#!/bin/bash
echo 'install logs:' > install.log 2>&1
sudo apt install  -qq -y figlet >> install.log 2>&1
figlet "Ancient Vision"
echo "The future of archeological databases and scanning software"
echo "By Ethan Li"
echo "MIT License"
cd
echo 'Installation Logs:'
echo 'Checking for and removing old install files'
figlet "Ancient Vision" >> install.log 2>&1
echo "The future of archeological databases and scanning software" >> install.log 2>&1
echo "By Ethan Li" >> install.log 2>&1
echo "MIT License" >> install.log 2>&1
echo 'Installation Logs:' >> install.log 2>&1
echo 'Checking for and removing old install files' >> install.log 2>&1
rm -f -- vision.py >> install.log 2>&1
rm -f -- DRV8825.py >> install.log 2>&1
rm -f -- service.py >> install.log 2>&1
rm -f -- stop.py >> install.log 2>&1
rm -f -- service.sh >> install.log 2>&1
rm -f -- requierments.txt >> install.log 2>&1
rm -f -- index.html >> install.log 2>&1
echo 'All old install files removed, pulling new ones'
echo 'All old install files removed, pulling new ones' >> install.log 2>&1
wget https://artifactalliance.org/install/vision.py -4 >> install.log 2>&1
wget https://artifactalliance.org/install/DRV8825.py -4 >> install.log 2>&1
wget https://artifactalliance.org/install/service.py -4 >> install.log 2>&1
wget https://artifactalliance.org/install/stop.py -4 >> install.log 2>&1
wget https://artifactalliance.org/install/service.sh -4 >> install.log 2>&1
wget https://artifactalliance.org/install/requierments.txt -4 >> install.log 2>&1
wget https://artifactalliance.org/install/index.html -4 >> install.log 2>&1
echo 'Main Files pulled; setting service.sh as executable' >> install.log 2>&1
echo 'Main Files pulled; setting service.sh as executable'
chmod +x service.sh
rm images -r >> install.log 2>&1
mkdir images && cd images
rm -f -- click.mp3 >> install.log 2>&1
rm -f -- button.png >> install.log 2>&1
rm -f -- GUI.png >> install.log 2>&1
rm -f -- title.png >> install.log 2>&1
echo 'Downloading HTML5 Assets'
echo 'Downloading HTML5 Assets' >> install.log 2>&1
wget https://artifactalliance.org/install/click.mp3 -4 >> install.log 2>&1
wget https://artifactalliance.org/install/button.png -4 >> install.log 2>&1
wget https://artifactalliance.org/install/GUI.png -4 >> install.log 2>&1
wget https://artifactalliance.org/install/title.png -4 >> install.log 2>&1
cd
echo 'Installing requiered python packages'
echo 'Installing requiered python packages' >> install.log 2>&1
pip install -r requierments.txt --break-system-packages --disable-pip-version-check >> install.log 2>&1
echo 'Installing linux-wifi-hotspot' 
rm linux-wifi-hotspot -r >> install.log 2>&1
echo 'Cloning Repository'
git clone https://github.com/lakinduakash/linux-wifi-hotspot.git >> install.log 2>&1
cd linux-wifi-hotspot
echo 'Building App'
make >> install.log 2>&1
sudo make install >> install.log 2>&1
systemctl enable create_ap >> install.log 2>&1
cd
echo "Installation complete! You can find the logs at install.log"
echo "The dashboard is hosted at http://localhost:1234"
echo "Set service.sh to run on startup!"
echo "Flask App Logs:"
python service.py || python3 service.py > flask.log
