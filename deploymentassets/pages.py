from flask import *
import os

app = Flask(__name__)

@app.route('/<folder1>/')
def fetchfolderindex(folder1):
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, folder1, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

@app.route('/<folder1>/<folder2>/')
def fetchfolderfolderindex(folder1, folder2):
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, folder1, folder2, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

@app.route('/<file1>')
def fetchfile(file1):
	if "." in file1:
		try:
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, file1)
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		except Exception as e:
			print(f"Error: {e}")
			return send_from_directory('', file1, as_attachment=False)
	else:
		root = os.path.dirname(__file__)
		file_path = os.path.join(root, file1, 'index.html')
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
      
@app.route('/<folder1>/<file1>')
def fetchfolderfile(folder1, file1):
	if "." in file1:
		try:
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, folder1, file1)
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		except Exception as e:
			print(f"Error: {e}")
			return send_from_directory(folder1, file1, as_attachment=False)
	else:
		root = os.path.dirname(__file__)
		file_path = os.path.join(root, folder1, file1, 'index.html')
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
    
@app.route('/<folder1>/<folder2>/<file1>')
def fetchfolderfolderfile(folder1, folder2, file1):
	if "." in file1:
		try:
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, folder1, folder2, file1)
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		except Exception as e:
			print(f"Error: {e}")
			return send_from_directory(folder1 + '/' + folder2, file1, as_attachment=False)
	else:
		root = os.path.dirname(__file__)
		file_path = os.path.join(root, folder1, folder2, file1, 'index.html')
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
      
@app.route('/')
def fetchindex():
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

@app.errorhandler(404)
def page_not_found(e):
	with open('404.html', 'r') as file:
		content = file.read()
	return content

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=False)
