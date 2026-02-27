#!/bin/bash
sudo apt install  -y -qq figlet
figlet "ANCIENT VISION"
echo "By Ethan Li"
echo "MIT 2.0 License"
cd
wget https://artifact-alliance.vercel.app/install/vision.py -nv -q
wget https://artifact-alliance.vercel.app/install/DRV8825.py -nv -q
wget https://artifact-alliance.vercel.app/install/service.py -nv -q
wget https://artifact-alliance.vercel.app/install/stop.py -nv -q
wget https://artifact-alliance.vercel.app/install/service.sh -nv -q
wget https://artifact-alliance.vercel.app/install/requierments.txt -nv -q
chmod +x service.sh
mkdir images
cd images
wget https://artifact-alliance.vercel.app/install/click.mp3 -nv -q
wget https://artifact-alliance.vercel.app/install/button.png -nv -q
wget https://artifact-alliance.vercel.app/install/GUI.png -nv -q
wget https://artifact-alliance.vercel.app/install/title.png -nv -q
cd
pip install -r -qq requierments.txt --break-system-packages --disable-pip-version-check
echo "Installation complete! The dashboard is hosted at http://localhost:1234"
echo "Also, set service.sh to run on startup!"
python service.py