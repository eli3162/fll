from flask import *
import logging, os, json, subprocess, pathlib, requests, uuid, logging, sys, textwrap, hashlib
from subprocess import *
from werkzeug.utils import secure_filename
from pathlib import Path
from logging.handlers import RotatingFileHandler
from collections import deque
from icmplib import ping

scanner_ip = '71.230.251.141'

passcode = "password"

def md5hash(passcode):
	res = hashlib.md5(passcode.encode())
	return res.hexdigest()

hashed_passcode = md5hash(passcode)

def is_ip_up(ip):
    try:
        host = ping(ip, count=1, timeout=2)
        return host.is_alive
    except:
        return False

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

@app.route('/generate_metadata/<filename>')
def generate_metadata(filename):
	data = {
		"Name": filename,
		"Description": None,
		"Code": "123456789",
		"UUID": str(uuid.uuid4()),
		"pointers": {
			"arobject": "/assets/" + filename + ".arobject",
			"model": "/assets/" + filename + ".obj",
			"thumbnail": "/assets/" + filename + ".png",
			"metadata": "/assets/" + filename + "_metadata.json"
		}
	}

	Path('assets').mkdir(parents=True, exist_ok=True)
	metadata_path = os.path.join(os.path.dirname(__file__), 'assets', f"{filename}.json")
	with open(metadata_path, 'w') as f:
		json.dump(data, f)

	return jsonify(data)

@app.route("/metadata/<filename>/<dict>")
def fetch_metadata(filename, dict):
	with open(os.path.join(os.path.dirname(__file__), 'assets', filename + ".json"), 'r') as f:
		data = json.load(f)
	return jsonify(data.get(dict))

@app.route("/metadata/<filename>/<dict>/<part>")
def fetch_dict(filename, dict, part):
	with open(os.path.join('assets', filename + ".json"), 'r') as f:
		data = json.load(f)
	return jsonify(data.get(dict, {}).get(part))

@app.route('/logs')
def get_logs():
	log_path = os.path.join(os.path.dirname(__file__), 'tmp/app.log')
	with open(log_path, 'r') as f:
		log_content = f.read()
	return f"<pre>{log_content}</pre>"

@app.route('/ip')
def get_ip():
	response = requests.get('https://api.ipify.org?format=json')
	ip_data = response.json()
	return ip_data

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

@app.route('/plan')
def plan():
	return 'https://mermaid.ai/d/f8036d0a-5254-49a9-95b5-142bff42174c'

@app.route('/dashboard')
def dashboard():
	with open('dashboard.html', 'r') as file:
		content = file.read()
	return content

@app.route('/setip/<ip>')
def set_ip(ip):
	global scanner_ip
	scanner_ip = ip
	return f"Scanner IP set to {ip}"

@app.route('/scanner_online')
def scanner_status():
	global scanner_ip
	if is_ip_up(scanner_ip):
		return "Scanner is online at " + scanner_ip
	else: 
		return "Scanner is offline but was last seen at " + scanner_ip

@app.route('/scanner_content')
def scanner_content():
	global scanner_ip
	content = f"""
Scanner IP: {scanner_ip}
Scanner Status: {"Online" if is_ip_up(scanner_ip) else "Offline"}
Scanner Name: ancientvision
Version: 4
	"""
	return content

@app.route('/passcode')
def get_passcode():
	return hashed_passcode

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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)