#!/bin/bash
sudo apt install  -qq -y figlet 
figlet "Ancient Vision"
echo "The future of archeological databases and scanning software"
echo "By Ethan Li"
echo "MIT License"
cd
echo 'Installation Logs:'
echo 'Checking for and removing old install files'
figlet "Ancient Vision" 
echo "The future of archeological databases and scanning software" 
echo "By Ethan Li" 
echo "MIT License" 
echo 'Installation Logs:' 
echo 'Checking for and removing old install files' 
rm -f -- vision.py 
rm -f -- powermonitor.py 
rm -f -- gpiolibrary.py 
rm -f -- service.py 
rm -f -- stop.py 
rm -f -- service.sh 
rm -f -- requierments.txt 
rm -f -- index.html 
echo 'All old install files removed, pulling new ones'
echo 'All old install files removed, pulling new ones' 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/vision.py 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/powermonitor.py 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/gpiolibrary.py 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/service.py 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/stop.py 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/service.sh 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/requierments.txt 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/index.html 
echo 'Main Files pulled; setting service.sh as executable' 
echo 'Main Files pulled; setting service.sh as executable'
chmod +x service.sh
rm images -r 
mkdir images && cd images
rm -f -- click.mp3 
rm -f -- button.png 
rm -f -- GUI.png 
rm -f -- title.png 
rm -f -- tailwind.js 
rm -f -- stop.png 
echo 'Downloading HTML5 Assets'
echo 'Downloading HTML5 Assets' 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/click.mp3 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/button.png 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/GUI.png 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/title.png 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/tailwind.js 
wget https://raw.githubusercontent.com/artifact-alliance/fll/master/install/stop.png 
cd
echo 'Installing requiered python packages'
echo 'Installing requiered python packages' 
pip install -r requierments.txt --break-system-packages --disable-pip-version-check 
echo 'Installing linux-wifi-hotspot' 
rm linux-wifi-hotspot -r 
echo 'Cloning Repository'
git clone https://github.com/lakinduakash/linux-wifi-hotspot.git 
cd linux-wifi-hotspot
echo 'Building App'
make 
sudo make install 
systemctl enable create_ap 
cd
echo "Installation complete! You can find the logs at install.log"
echo "The dashboard is hosted at http://localhost:1234"
echo "Set service.sh to run on startup!"
echo "Flask App Logs:"
python service.py || python3 service.py > flask.log
