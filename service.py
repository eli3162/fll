from flask import *
import os, time


app = Flask(__name__)

@app.route('/')
def home():
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

@app.route('/images/<filename>')
def image_fetch(filename):
        return send_from_directory('images', filename, as_attachment=True)

@app.route('/scan/')
def scan():
        os.system('python vision.py')
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

@app.route('/stop/')
def stopplease():
        os.system('pkill -f vision.py')
        time.sleep(0.2)
        os.system('python stop.py')
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
@app.route('/meta/')
def metadata():
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'view.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()      

@app.route('/<filename>')
def file_fetch(filename):
        return send_from_directory('', filename, as_attachment=True)

@app.route('/attachmetadata/<data>')
def attach_metadata(data):
        metadata[len(metadata)] = data
        return 'Metadata attached successfully'

@app.route('/resetmetadata/')
def reset_metadata():
        metadata.clear()
        return 'Metadata reset successfully'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)