import requests, os, time, glob, uuid           
import aspose.threed as a3d
from pathlib import Path

scan_name= uuid.uuid4()
scanner_ip = '192.168.12.1'

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


def photogrammetryoperation(scanname=uuid.uuid4(), scannerip='192.168.12.1'):
    os.chdir(os.path.dirname(__file__))

    try:
        os.mkdir('.photogrammetrycache')
    except FileExistsError:
        pass

    for file in glob.glob('.photogrammetrycache/output*'):
        os.remove(file)

    for file in glob.glob('.photogrammetrycache/processing*'):
        os.remove(file)

    file_path = Path(".photogrammetrycache/processor")
    if file_path.is_file():
        print("File exists")
    else:
        download_file('https://github.com/artifact-alliance/fll/raw/refs/heads/main/deploymentassets/processor', '.photogrammetrycache/processor')

    for i in range(160):
        download_file(f'http://{scanner_ip}:1234/images/captured_img{i}.png', f'.photogrammetrycache/processing{i}.png')

    os.system(f'.photogrammetrycache/processor .photogrammetrycache/ {scan_name}.usdz -d raw')

    for file in glob.glob('.photogrammetrycache/processing*'):
        os.remove(file)

    scene = a3d.Scene.from_file(f"{scan_name}.usdz")
    scene.save(f"output{scan_name}.glb")
    scene.save(f"output{scan_name}.ply")
    time.sleep(0.1)
    os.remove(f"{scan_name}.usdz")
    return[f".photogrammetrycache/output{scan_name}.glb", f".photogrammetrycache/output{scan_name}.ply"]

photogrammetryoperation(scanname=scan_name, scannerip=scanner_ip)