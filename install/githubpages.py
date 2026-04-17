from flask import *
from subprocess import *
import requests
from werkzeug.utils import secure_filename
import os
import json
import subprocess
from pathlib import Path

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

@app.route('/directory/')
def folderindex(directory):
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, directory, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

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
