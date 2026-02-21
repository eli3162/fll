import webbrowser, os, sys, shutil, asyncio, time
async def main():
    ip = input("IP: ")
    pic_count = input("Picture Count: ")
    try:
        for i in range(1, int(pic_count) + 1):
            os.remove(r"C:\Users\Public\images\captured_img" + str(i) + ".jpg")

    except FileNotFoundError:
        pass
    time.sleep(1)
    for j in range(1, int(pic_count) + 1):
        webbrowser.open("http://" + ip + ":5000/images/captured_img" + str(j) + ".jpg")
    time.sleep(10)
    for k in range(1, int(pic_count) + 1):
        shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img' + str(k) + '.jpg', r"C:\Users\Public\images\captured_img" + str(k) + ".jpg")
    time.sleep(100)
    try:
        for i in range(1, int(pic_count) + 1):
            os.remove(r"C:\Users\Ethan Li\Downloads\captured_img" + str(i) + ".jpg")
    except FileNotFoundError:
        pass

asyncio.run(main())

os.system(r'"C:\Users\Public\Meshroom2025\Meshroom2025\meshroom_compute.exe" "C:\Users\Public\scanner.mg"')

while not os.path.exists(r"C:\Users\Public\scanner\texturedMesh.obj"):
    pass

import trimesh
from trimesh.visual import resolvers

def convert_obj_to_glb(obj_path, mtl_path, texture_path, output_glb_path):
    """
    Load an OBJ with specified MTL and PNG texture paths, and export to GLB with embedded texture.
    """

    # Build a resolver from the folder where the MTL and texture live
    # Put mtl and texture folder location(s) here:
    base_resolver = resolvers.FilePathResolver('.')
    base_resolver = base_resolver.namespaced(mtl_path.rsplit('/', 1)[0])
    base_resolver = base_resolver.namespaced(texture_path.rsplit('/', 1)[0])

    # Load the scene using trimesh.load with the custom resolver
    scene = trimesh.load(obj_path, resolver=base_resolver, force='scene')

    # Export to GLB bytes (binary glTF with embedded textures)
    glb_bytes = scene.export(file_type='glb')

    # Write the GLB file
    with open(output_glb_path, 'wb') as f:
        f.write(glb_bytes)

    print(f"Converted '{obj_path}' + '{mtl_path}' + '{texture_path}' → '{output_glb_path}'")


if __name__ == "__main__":
    # Replace these with your actual paths
    input_obj     = r"C:\Users\Public\scanner\texturedMesh.obj"
    input_mtl     = r"C:\Users\Public\scanner\texturedMesh.mtl"
    input_texture = r"C:\Users\Public\Scans\texture1001.png"
    output_glb    = r"C:\Users\Ethan Li\OneDrive\Documents\website\fll\artifacts\scan.glb"

    convert_obj_to_glb(input_obj, input_mtl, input_texture, output_glb)
