#!/bin/bash
cd
wget https://artifact-alliance.vercel.app/install/vision.py
wget https://artifact-alliance.vercel.app/install/DRV8835.py
wget https://artifact-alliance.vercel.app/install/service.py
wget https://artifact-alliance.vercel.app/install/stop.py
wget https://artifact-alliance.vercel.app/install/service.sh
wget https://artifact-alliance.vercel.app/install/requirements.txt
mkdir images
cd images
wget https://artifact-alliance.vercel.app/install/click.mp3
wget https://artifact-alliance.vercel.app/install/button.png
wget https://artifact-alliance.vercel.app/install/GUI.png
wget https://artifact-alliance.vercel.app/install/title.png
cd
sudo apt install figlet
pip install -r requirements.txt
figlet "ANCIENT VISION"
echo "Installation complete! Reboot to start web server or run python service.py to start it now. The dashboard is hosted at http://localhost:1234"
(crontab -l 2>/dev/null; echo "@reboot /home/ancient_vision_root/service.sh") | crontab -