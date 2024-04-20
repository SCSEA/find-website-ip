# Code is here.
# Prophet Muhammad Peace and Blessing Be Upon Him.
# Alhamdulillah.
# Version 1.9.
# This code is foe Educational and Purpose Only...


import os
import socket
import time
#import time as t
import sys
import pyfiglet
import colorama
from tqdm import tqdm
from colorama import Fore, init, Back

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")
    os.system("pip install socket")
    os.system("pip install time")
    os.system("pip install tqdm")

# Clear the console screen
os.system("cls" if os.name == "nt" else "clear")



init(autoreset=True)

rd = colorama.Fore.RED
bl = colorama.Fore.BLUE
yl = colorama.Fore.YELLOW
#pl = colorama.Fore.PURPLE
mag = colorama.Fore.MAGENTA
gn = colorama.Fore.GREEN
cy = colorama.Fore.CYAN



# Regular text colors

black = "\033[0;30m"      # Black

red = "\033[0;31m"        # Red

green = "\033[0;32m"      # Green

yellow = "\033[0;33m"     # Yellow

blue = "\033[0;34m"       # Blue

purple = "\033[0;35m"     # Purple

cyan = "\033[0;36m"       # Cyan

white = "\033[0;37m"      # White



# Bold text colors

b_black = "\033[1;30m"    # Bold Black

b_red = "\033[1;31m"      # Bold Red

b_green = "\033[1;32m"    # Bold Green

b_yellow = "\033[1;33m"   # Bold Yellow

b_blue = "\033[1;34m"     # Bold Blue

b_purple = "\033[1;35m"   # Bold Purple

b_cyan = "\033[1;36m"     # Bold Cyan

b_white = "\033[1;37m"    # Bold White



# Underline text colors

u_black = "\033[4;30m"    # Underline Black

u_red = "\033[4;31m"      # Underline Red

u_green = "\033[4;32m"    # Underline Green

u_yellow = "\033[4;33m"   # Underline Yellow

u_blue = "\033[4;34m"     # Underline Blue

u_purple = "\033[4;35m"   # Underline Purple

u_cyan = "\033[4;36m"     # Underline Cyan

u_white = "\033[4;37m"    # Underline White



# Background colors

bg_black = "\033[40m"     # Background Black

bg_red = "\033[41m"       # Background Red

bg_green = "\033[42m"     # Background Green

bg_yellow = "\033[43m"    # Background Yellow

bg_blue = "\033[44m"      # Background Blue

bg_purple = "\033[45m"    # Background Purple

bg_cyan = "\033[46m"      # Background Cyan

bg_white = "\033[47m"     # Background White



# Reset text color

reset = "\033[0m"         # Reset



# ------ colors

r = "\033[1;31m"

g = "\033[1;32m"

y = "\033[1;33m"

b = "\033[1;34m"

d = "\033[2;37m"

R = "\033[1;41m"

Y = "\033[1;43m"

B = "\033[1;44m"

w = "\033[1;37m"

g = "\033[0;90m"

gg = "\033[1;32m"

y = r




# Simulating loading with a progress bar
for _ in tqdm(range(86609), desc=Fore.GREEN+'Accessing to the code server', unit='bytes', ascii=True):
    time.sleep(0.00001)  # Simulating processing time
#    time.sleep(2)
print("\n")
print(Fore.CYAN +"Done, complete!")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# Delay for displaying messages
delay = 1

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


                   <Program>  Find Website IP  </Program>


                 <Developer>  Saif Ullah   </Developer>


            <GitHub> https://github.com/SCSEA </GitHub>


         <Tiktok> tiktok.com/@programmer_boy_2 </Tiktok>

           
    <Telegram> https://t.me/programmerboy1 </Telegram>


___________________________________________________________________________
    """)

banner()


def BannerOptions():
    clear()
    banner()

def backslash():
    print('\n')

def clear():
    _ = os.system('cls' if os.name == 'nt' else 'clear')

def LoadingScreen(ask):
    print(blue + "└─ " + Fore.WHITE + f'{ask} ' + Fore.CYAN, end=" ", flush=True)
    for x in range(3):
        for frame in r'-\|/-\|/':
            print('\b', frame, sep="", end="", flush=True)
            time.sleep(0.2)
    print('\b')

def LoadingScreen_(ask):
    print(blue + "└─ " + Fore.WHITE + f'{ask} ' + Fore.CYAN, end=" ", flush=True)
    for x in range(1):
        for frame in r'-\|/-\|/':
            print('\b', frame, sep="", end="", flush=True)
            time.sleep(0.2)
    print('\b')

def update():
    print(Fore.BLUE + "Updating script from GitHub...")
    os.system('git pull')
    print(Fore.GREEN + "Update successful. Please restart the script.")
    sys.exit(0)

#def about_mee():
#    BannerOptions()
#    LoadingScreen('Loading Data')
#    
#    about_mee = Fore.GREEN + """Assalamu Alaikum, I’m @Yousuf Shafii Muhammad, a self-taught Programmer and Ethical Hacker and Developer Profissional in 100 Programming languages."""

#for i in about_mee :
#    sys.stdout.write(i)
#    sys.stdout.flush()
#    time.sleep(0.03)
#time.sleep(0.7)

#backslash()
#BannerOptions()



#def find_ip_address(url):
#    # Input target website
#    domain = input("Enter Target Website or url or domain (e.g., example.com, https://example.com, http://example.com or www.example.com to find IP Addreswcof that Website ): ")

#for domain in domains:
#        if url.startswith("http://") or domain.startswith("https://") or domain.startswith("www."):
#            domain = domain.replace("http://", "").replace("https://", "").replace("www.", "")

#else:
#  continue

 #   print("")
  #  time.sleep(2)
#    print(Fore.GREEN + "Getting IP Address attacking........")
#    time.sleep(2)
#    print(Fore.GREEN + "Getting IP Address  0%")
#    time.sleep(2)
 #   for i in range(10, 110, 10):
 #       print(Fore.GREEN + f"Getting IP Address  {i}%")
#        time.sleep(2)
#    print(Fore.GREEN + "IP Address Founded Successsfully")
#    time.sleep(2)
#    try:
#        print(Fore.GREEN + "IP Address is:", Fore.GREEN+socket.gethostbyname(url))
#    except socket.gaierror:
#        print(Fore.RED + f"Failed to resolve the host : {url}")
#        print(Fore.RED + "Failed to resolve the host")
 #   time.sleep(3)
#    print("")



#import socket
#import time
#from colorama import Fore

#def find_website_ip_address():
    # Input target website
#    domain = input("Enter Target Website or URL or Domain (e.g., example.com, https://example.com, http://example.com or www.example.com to find IP Address of that Website): ")

#    if "." not in domain:
#        print("You entered an invalid domain.\n Please enter a valid domain (e.g., www.example.com, http://example.com, https://example.com, example.com).\nPlease re-un the script python3 get-website-ip.py\n")
#        pass
#        return
#        find_website_ip_address()
#
#    if domain.startswith(("http://", "https://", "www.")):
#        domain = domain.replace("http://", "").replace("https://", "").replace("www.", "")
#
#    print("")
#    time.sleep(2)
#    print(Fore.GREEN + "Getting IP Address attacking........")
#    time.sleep(2)
#    print(Fore.GREEN + "Getting IP Address  0%")
#    time.sleep(2)
#    for i in range(10, 110, 10):
#        print(Fore.GREEN + f"Getting IP Address  {i}%")
#        time.sleep(2)
#    print(Fore.GREEN + "IP Address Founded Successfully")
#    time.sleep(2)
#    try:
#        print(Fore.GREEN + "IP Address is:", Fore.GREEN + socket.gethostbyname(domain))
#    except socket.gaierror:
#        print(Fore.RED + f"Failed to resolve the host : {domain}")
#    print("")

# Example usage:
#find_ip_address()


#cont = input(Fore.YELLOW +  "Do you wanna continue?[n/y]: ")
#if cont == "Y" or cont == "y":
#    banner()
#banner()

#def about_me():

import time
import socket
from colorama import Fore

def timestamp():
#    return time.strftime("%b %d %H:%M:%S.%f")
    return time.strftime("%b %d %H:%M:%S")

def find_website_ip_address():
    # Input target website
    domain = input(Fore.CYAN+ "Enter Target Website or URL or Domain (e.g., example.com, https://example.com, http://example.com or www.example.com to find IP Address of that Website): ")

    if "." not in domain:
        print(Fore.RED+ "You entered an invalid domain.\n Please enter a valid domain (e.g., www.example.com, http://example.com, https://example.com, example.com).\nPlease re-run the script python3 get-website-ip.py\n")
        pass
        return
        find_website_ip_address()

    if domain.startswith(("http://", "https://", "www.")):
        domain = domain.replace("http://", "").replace("https://", "").replace("www.", "")

    print("")
    time.sleep(2)
    print(Fore.GREEN + timestamp() + " Getting IP Address attacking........")
    time.sleep(2)
    print(Fore.GREEN + timestamp() + " Getting IP Address  0%")
    time.sleep(2)
    for i in range(10, 110, 10):
        print(Fore.GREEN + timestamp() + f" Getting IP Address  {i}%")
        time.sleep(2)
    print(Fore.GREEN + timestamp() + " IP Address Found Successfully")
    time.sleep(2)
    try:
        print(Fore.GREEN + timestamp() + " IP Address is:", Fore.GREEN + socket.gethostbyname(domain))
    except socket.gaierror:
        print(Fore.RED + timestamp() + f" Failed to resolve the host : {domain}")
    print("")

#find_website_ip_address()


def about_me():
    BannerOptions()
    LoadingScreen('Loading Data')
    BannerOptions()
    about_me_text = Fore.GREEN +"""Assalamu Alaikum, I’m @Saif Ullah, Programmer and Ethical Hacker and Developer and Software-engineer. i know more than 100 Programming languages."""

    for i in about_me_text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
    
    time.sleep(0.7)

	

	#about_me = Fore.GREEN + """Assalamu Alaikum, I’m @Yousuf Shafii Muhammad, a self-taught Programmer and Ethical Hacker and Developer Profissional in 100 Programming languages."""

#for i in about_me :
#    sys.stdout.write(i)
#    sys.stdout.flush()
#    time.sleep(0.03)
#time.sleep(0.7)

backslash()

while True:
    choice = input(Fore.BLUE + "Choose an option:\n1. Find IP address of a website\n2. Update script\n3. About Me\n4. Exit\nEnter option number: ")

    if choice == '1':
        find_website_ip_address()
        exit()
    elif choice == '2':
        update()
        exit()
    elif choice == '3':
        about_me()
        exit()
    elif choice == '4':
        sys.exit(0)
    else:
        print(Fore.RED + "Invalid option. Please try again.")



cont = input(Fore.YELLOW +  "Do you want to continue ? [n/y] : ")
if cont == "Y" or cont == "y":
    banner()
banner()
