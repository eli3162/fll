from flask import *
from subprocess import *
import requests
from werkzeug.utils import secure_filename
import os
import json
import subprocess
from pathlib import Path

def terminal_run(cmd, timeout=None, shell=False):
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        shell=shell,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr

def send_file(url, file_path, field_name='file', extra_data=None):
    file_path = Path(file_path)
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    files = {field_name: (file_path.name, open(file_path, 'rb'))}
    data = extra_data or {}
    try:
        resp = requests.post(url, files=files, data=data)
        resp.raise_for_status()
        return resp
    finally:
        files[field_name][1].close()

def get(url, timeout=10):
    resp = requests.get(url, stream=True, timeout=timeout)
    try:
        resp.raise_for_status()
        return resp
    finally:
        resp.close()


def download_file(url, local_filename):
    local_filename = os.path.join(os.path.dirname(__file__), local_filename)
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk: 
                        f.write(chunk)
	    
        return local_filename
    except requests.exceptions.RequestException as e:
        return e

app = Flask(__name__)

@app.route('/<directory>', methods=['GET', 'POST'])
def upload(directory):
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return 'No file selected'
            
            file = request.files['file']
            if file.filename == '':
                return 'No file selected'
            
            if file:
                upload_dir = os.path.join(os.path.dirname(__file__), directory)
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                filename = secure_filename(file.filename)
                file_path = os.path.join(upload_dir, filename)

                file.save(file_path)

                return f'File {filename} uploaded successfully!'
        
        except Exception as e:
            return f'An error occurred: {e}'
    
    return 'Upload to this API in type: multipart/form-data'
    
@app.route('/<file>')
def index(file):
	if file not in ['favicon.ico']:
		try:
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, file)
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		except Exception as e:
			print(f"Error: {e}")
			return send_from_directory('', file, as_attachment=False)
	else:
		return send_from_directory('', file, as_attachment=False)
      
@app.route('/<file1>/<file2>')
def index2(file1, file2):
	try:
		root = os.path.dirname(__file__)
		file_path = os.path.join(root, file1, file2)
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
	except Exception as e:
		print(f"Error: {e}")
		return send_from_directory(file1, file2, as_attachment=False)
    
@app.route('/<file1>/<file2>/<file3>')
def index3(file1, file2, file3):
	try:
		root = os.path.dirname(__file__)
		file_path = os.path.join(root, file1, file2)
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
	except Exception as e:
		print(f"Error: {e}")
		return send_from_directory(file1 + '/' + file2, file3, as_attachment=False)
      
@app.route('/')
def home():
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=False)