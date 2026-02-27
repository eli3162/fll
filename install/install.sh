#!/bin/bash
echo "MIT 2.0 License"
cd
wget https://artifact-alliance.vercel.app/install/vision.py -nv
wget https://artifact-alliance.vercel.app/install/DRV8835.py -nv
wget https://artifact-alliance.vercel.app/install/service.py -nv
wget https://artifact-alliance.vercel.app/install/stop.py -nv
wget https://artifact-alliance.vercel.app/install/service.sh -nv
wget https://artifact-alliance.vercel.app/install/requierments.txt -nv
chmod +x service.sh
mkdir images
cd images
wget https://artifact-alliance.vercel.app/install/click.mp3 -nv
wget https://artifact-alliance.vercel.app/install/button.png -nv
wget https://artifact-alliance.vercel.app/install/GUI.png -nv
wget https://artifact-alliance.vercel.app/install/title.png -nv
cd
sudo apt install figlet -y -qq
pip install -r requierments.txt --break-system-packages -qq
figlet "- ANCIENT VISION -"
echo "Installation complete! Run python service.py to start it now. The dashboard is hosted at http://localhost:1234"
echo "Also, set service.sh to run on startup!"