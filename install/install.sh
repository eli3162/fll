#!/bin/bash
sudo apt install  -qq -y figlet
figlet "Ancient Vision"
echo "The future of archeological databases and scanning software"
echo "By Ethan Li"
echo "MIT License"
cd
echo 'Checking for and removing old install files'
rm -f -- vision.py >/dev/null 2>&1
rm -f -- DRV8825.py >/dev/null 2>&1
rm -f -- service.py >/dev/null 2>&1
rm -f -- stop.py >/dev/null 2>&1
rm -f -- service.sh >/dev/null 2>&1
rm -f -- requierments.txt >/dev/null 2>&1
rm -f -- index.html >/dev/null 2>&1
echo 'All old install files removed, pulling new ones'
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/vision.py -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/DRV8825.py -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/service.py -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/stop.py -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/service.sh -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/requierments.txt -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/index.html -nv -q
echo 'Main Files pulled; setting service.sh as executable'
chmod +x service.sh
rm images -r >/dev/null 2>&1
mkdir images && cd images
rm -f -- click.mp3 >/dev/null 2>&1
rm -f -- button.png >/dev/null 2>&1
rm -f -- GUI.png >/dev/null 2>&1
rm -f -- title.png >/dev/null 2>&1
echo 'Downloading HTML5 Assets'
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/click.mp3 -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/button.png -nv -q
wget https://raw.githubusercontent.com/eli3162/fll/refs/heads/main/install/GUI.png -nv -q
cd
echo 'Installing requiered python packages'
pip install -r requierments.txt --break-system-packages --disable-pip-version-check -qq
echo 'Installing linux-wifi-hotspot'
rm linux-wifi-hotspot -r >/dev/null 2>&1
echo 'Cloning Repository'
git clone --quiet https://github.com/lakinduakash/linux-wifi-hotspot
cd linux-wifi-hotspot
echo 'Building App'
make --silent
sudo make install
cd
echo "Installation complete! The dashboard is hosted at http://localhost:1234"
echo "Set service.sh to run on startup!"
echo "Flask App Logs:"
python service.py -qq || python3 service.py -qq
