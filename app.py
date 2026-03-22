from flask import *
import logging, os, json, subprocess, pathlib, requests, uuid, logging, sys, textwrap, hashlib
from subprocess import *
from werkzeug.utils import secure_filename
from pathlib import Path
from logging.handlers import RotatingFileHandler
from collections import deque

scanner_ip = '71.230.251.141'

def parse(data):
    marker = "#path.fll-DATA"

    idx = data.find(marker)
    if idx != -1:
        data = data[:idx].rstrip("\r\n")

    data = data.replace("#PATH-POINTS-START Path", "")

    data = str(data)

    lines = data.splitlines()

    lines = [ln for ln in lines if ln.strip() != ""]

    wrapped = []
    for i, ln in enumerate(lines):
        parts = [p.strip() for p in ln.split(',') if p.strip() != '']
        if len(parts) > 3:
            parts = parts[:3]
        if len(parts) >= 3:
            try:
                v = float(parts[2])
                v = v / 120.0
                if v.is_integer():
                    parts[2] = str(int(v))
                else:
                    parts[2] = ('%f' % v).rstrip('0').rstrip('.')
            except Exception:
                pass
        elem_content = ','.join(parts)
        elem = '[' + elem_content + ']'
        if i != len(lines) - 1:
            elem += ','
        wrapped.append(elem)

    data = textwrap.indent("\n".join(wrapped), "    ")

    data = '[\n' + data + '\n]'

    data = textwrap.indent(data, "    ")

    data = '{"path": ' + '\n' + data + '\n}'
    return data

app = Flask(__name__)


@app.route('/')
def index():
	with open('index.html', 'r') as file:
		content = file.read()
	return content

@app.route('/<filename>')
def serve_file(filename):
	return send_from_directory('.', filename)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
	if 'file' not in request.files:
		return 'No file part', 400
	file = request.files['file']
	if file.filename == '':
		return 'No selected file', 400
	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join('assets', filename))
		return 'File uploaded successfully', 200

@app.route('/assets/<filename>')
def serve_artifact(filename):
	return send_from_directory('assets', filename)

@app.route('/models/<filename>')
def serve_model(filename):
	return send_from_directory('models', filename)

@app.route('/convert', methods=['POST', 'GET'])
def parse_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			return 'No file part', 400
		file = request.files['file']
		if file.filename == '':
			return 'No selected file', 400
		if file:
			content = file.read().decode('utf-8')
			parsed_data = parse(content)
			return parsed_data, 200
	else: 
		with open('parse.html', 'r') as file:
			content = file.read()
		return content

@app.route('/dashboard')
def dashboard():
	with open('dashboard.html', 'r') as file:
		content = file.read()
	return content

@app.route('/login')
def login():
	with open('login.html', 'r') as file:
		content = file.read()
	return content

@app.route('/artifacts')
def artifacts():
	with open('artifacts.html', 'r') as file:
		content = file.read()
	return content

@app.route('/app')
def applogin():
	with open('login.html', 'r') as file:
		content = file.read()
	return content

@app.route('/poll')
def poll():
	with open('poll.html', 'r') as file:
		content = file.read()
	return content

@app.route('/scripts/<filename>')
def serve_script(filename):
	return send_from_directory('scripts', filename)


@app.route('/view/<filename>')
def view(filename):
	with open('view.html', 'r') as file:
		content = file.read()
	return content

@app.route('/data/<filename>')
def data(filename):
	try:
		with open(os.path.join(os.path.dirname(__file__), 'metadata', filename), 'r') as f:
			data = json.load(f)
		return jsonify(data)
	except Exception as e:
		return jsonify({"error": str(e)}), 404

@app.route('/install/<filename>')
def installer_file(filename):
	return send_from_directory('install', filename, as_attachment=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)