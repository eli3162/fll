#!/bin/bash
sudo apt install  -qq -y figlet
figlet "ANCIENT VISION"
echo "By Ethan Li"
echo "MIT License"
cd
rm -f -- vision.py >/dev/null 2>&1
rm -f -- DRV8825.py >/dev/null 2>&1
rm -f -- service.py >/dev/null 2>&1
rm -f -- stop.py >/dev/null 2>&1
rm -f -- service.sh >/dev/null 2>&1
rm -f -- requierments.txt >/dev/null 2>&1
rm -f -- index.html >/dev/null 2>&1
wget https://artifact-alliance.vercel.app/install/vision.py -nv -q
wget https://artifact-alliance.vercel.app/install/DRV8825.py -nv -q
wget https://artifact-alliance.vercel.app/install/service.py -nv -q
wget https://artifact-alliance.vercel.app/install/stop.py -nv -q
wget https://artifact-alliance.vercel.app/install/service.sh -nv -q
wget https://artifact-alliance.vercel.app/install/requierments.txt -nv -q
wget https://artifact-alliance.vercel.app/install/index.html -nv -q
chmod +x service.sh
rm images -r >/dev/null 2>&1
mkdir images && cd images
rm -f -- click.mp3 >/dev/null 2>&1
rm -f -- button.png >/dev/null 2>&1
rm -f -- GUI.png >/dev/null 2>&1
rm -f -- title.png >/dev/null 2>&1
wget https://artifact-alliance.vercel.app/install/click.mp3 -nv -q
wget https://artifact-alliance.vercel.app/install/button.png -nv -q
wget https://artifact-alliance.vercel.app/install/GUI.png -nv -q
wget https://artifact-alliance.vercel.app/install/title.png -nv -q
cd
pip install -r requierments.txt --break-system-packages --disable-pip-version-check -qq
echo "Installation complete! The dashboard is hosted at http://localhost:1234"
echo "Set service.sh to run on startup!"
python service.py -qq || python3 service.py -qq