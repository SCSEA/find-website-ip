# find-website-ip

Server IP (Internet Protocol) address is an inseparable part of everything connected on the internet. Its purpose is to make it easy to properly recognize a specific place on the internet where the information is supposed to be sent and received.

Before 2011, IPs were following a format of a set of 4 numbers separated by dots. Each number is 1-3 digits long with a value from 0-255. This was called the IPv4 or Internet protocol version 4 format.

However, since 2011, we have exhausted the IPv4 and are now using the IPv6 format that looks a bit like this 2600:1005:b062:61e4:74d7:f292:802c:fbfd.

Server IP address displayed on the screen

But what’s important for you, is to know that servers assign specific IP addresses also to websites like yours. Also, depending on your hosting, you can get either a shared or dedicated IP address.

# Installation

apt update && apt upgrade -y

pkg install git

pkg install python3

git clone https://github.com/SCSEA/find-website-ip.git

cd find-website-ip

pip3 install -r requirements.txt

chmod 777 get-website-ip.py

chmod +x * get-website-ip.py

python3 get-website-ip.py

