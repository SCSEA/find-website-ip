import os
import socket
import time
import sys
import pyfiglet
import colorama
from colorama import Fore, init

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install socket")
    os.system("pip install time")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")

# Clear the console screen
os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)

# Delay for displaying messages
delay = 7

# Legal disclaimer
print(Fore.BLUE + "[!] Legal Disclaimer : Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")
print("")
print(Fore.BLUE + "[+] I hope for you good future and i am willing that you will come high effort.")
time.sleep(delay)
print("")

# Print ASCII art
fg = pyfiglet.Figlet(font="standard").renderText("Find-website-ip")
print(Fore.CYAN + fg)
print("")



def banner():

    print(Fore.LIGHTBLUE_EX + """

___________________________________________________________________________

                                                                                                                      >

                   <Program>  Find Website IP  </Program>



                 <Developer>  Yousuf Shafii Muhammad  </Developer>



            <GitHub> https://github.com/SCSEA </GitHub>



           <Tiktok> tiktok.com/@programmer_boy_2 </Tiktok>



___________________________________________________________________________



    """)

banner()


# Input target website
url = input(Fore.BLUE + "Enter Target Website: ")
print("")
time.sleep(1)
print(Fore.GREEN + "Getting IP Address Attacking &&& Accessing &&& Injecting 😀.......")
time.sleep(2)

# Simulate progress
for i in range(0, 110, 10):
    print(Fore.GREEN + f"Getting IP Address {i}%")
    time.sleep(2)

# Get and print IP address
try:
    ip_address = socket.gethostbyname(url)
    print(Fore.GREEN + "IP Address Found Successfully")
    print(Fore.GREEN + "IP Address is:", ip_address)
except socket.gaierror:
    print(Fore.RED + "Failed to resolve the host")

print("")

