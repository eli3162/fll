#!/bin/bash
echo "MIT 2.0 License"
cd
wget https://artifact-alliance.vercel.app/install/vision.py
wget https://artifact-alliance.vercel.app/install/DRV8835.py
wget https://artifact-alliance.vercel.app/install/service.py
wget https://artifact-alliance.vercel.app/install/stop.py
wget https://artifact-alliance.vercel.app/install/service.sh
wget https://artifact-alliance.vercel.app/install/requierments.txt
chmod +x service.sh
mkdir images
cd images
wget https://artifact-alliance.vercel.app/install/click.mp3
wget https://artifact-alliance.vercel.app/install/button.png
wget https://artifact-alliance.vercel.app/install/GUI.png
wget https://artifact-alliance.vercel.app/install/title.png
cd
sudo apt install figlet
pip install -r requierments.txt --break-system-packages
figlet "- ANCIENT VISION -"
echo "Installation complete! Run python service.py to start it now. The dashboard is hosted at http://localhost:1234"
echo "Also, set service.sh to run on startup!"