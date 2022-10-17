import sys

#Remove comments, if you want this to install requirements right after running
#def install(package):
    #subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#for x in ["keyboard", "fernet", "cryptography", "colorama", "tk"]:
    #install(x)

import os
import random
from string import ascii_letters
import time
import keyboard
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import tkinter
from tkinter import filedialog
import platform
from colorama import init, Fore, Back, Style
import base64
init(convert=True)


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(Fore.CYAN + Style.BRIGHT + f"---->  {filename} is now encrypted!")
    time.sleep(2.5)
    os.system('cls')
def generate_keys(length, filename, encrypt_type):
    if encrypt_type == '-r':
        letters = []
        for x in ascii_letters:
            letters.append(x)
        for n in range(9):
            letters.append(str(n))
        keys = ""
        for _ in range(length):
            keys = keys + random.choice(letters)
        os.system('cls')
        print(Fore.WHITE + Style.BRIGHT + "Setting password to : " + Fore.GREEN + Style.BRIGHT + keys + Fore.YELLOW + Style.BRIGHT + "   -----> " + filename)
        print(Fore.WHITE + Style.BRIGHT + "Press space to continue...")
        keyboard.wait("space")
        keys = keys.encode("utf-8")
        password = b"%b" % keys
    elif encrypt_type == "-o":
        os.system('cls')
        system = platform.system()
        username = os.getlogin()
        if system == "Windows":
            check = os.path.exists(f"C:\\Users\\{username}\\AppData\\Local\\Temp")
            if check == True:
                os.system(f"type > nul C:\\Users\\{username}\\AppData\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt")
                open_temp = open(f"C:\\Users\\{username}\\AppData\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt", "wb")
                passwrd = sys.argv[2]
                passwrd = base64.b64encode(passwrd.encode('utf-8'))
                open_temp.write(passwrd)
        print(Fore.WHITE + Style.BRIGHT + "Setting password to : " + Fore.GREEN + Style.BRIGHT + sys.argv[2] + Fore.YELLOW + Style.BRIGHT + "   -----> " + filename)
        print(Fore.WHITE + Style.BRIGHT + "Press space to continue...")
        keyboard.wait("space")
        passwd = sys.argv[2].encode("utf-8")
        password = b"%b" % passwd

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    secret_in_string = str(key)
    leng = len(secret_in_string) - 1
    secret_in_string = secret_in_string[2:leng]
    print(Fore.WHITE + Style.BRIGHT + "Secret:  " + Fore.GREEN + Style.BRIGHT + secret_in_string)
    print(Fore.WHITE + Style.BRIGHT + "Press space to continue...")
    keyboard.wait("space")
    os.system("cls")
    encrypt(filename, key)
    
def main():
    system = platform.system()
    usage = f"""Usage: python3 {sys.argv[0]} <type>.
        Types: 
        
        -o  Your own password
        -r  Random password"""
    if ".py" in sys.argv[0]:
        try:
            encrypt_type = sys.argv[1]
        except IndexError:
            os.system('cls')
            print(Fore.GREEN + Style.BRIGHT + usage)
            sys.exit(1)
    elif ".exe" in sys.argv[0]:
        encrypt_type = input(Fore.GREEN + Style.DIM + "Encryption type:  " + Fore.BLUE + Style.BRIGHT + "-o" + Fore.GREEN + Style.DIM + " = own password or " + Fore.CYAN + Style.BRIGHT + "-r" + Fore.GREEN + Style.DIM + " = random password\n ------>  ")
        tkinter.Tk().withdraw()
        file_path = filedialog.askopenfilenames()
        file_list = []
        for files in file_path:
            file_list.append(files)
        if encrypt_type == "-o":
            x = 0
            for i in file_list:
                generate_keys(x, i, encrypt_type)
        elif encrypt_type == "-r":
            os.system("cls")
            leng = 10
            for i in file_list:
                generate_keys(leng, i, encrypt_type)

    if len(sys.argv) < 2:
        os.system("cls")
        print(Fore.GREEN + Style.BRIGHT + usage)
        print("Press space to continue...")
        keyboard.wait('space')
        os.system('cls')
        main()
    tkinter.Tk().withdraw()
    file_path = filedialog.askopenfilenames()
    file_list = []
    for files in file_path:
        file_list.append(files)
    if encrypt_type == "-o":
        try:
            sys.argv[2]
            x = ""
            for i in file_list:
                generate_keys(x, i, encrypt_type)
        except IndexError:
            os.system('cls')
            print(Fore.GREEN + Style.BRIGHT + f"""Usage: python3 {sys.argv[0]} -o <password>""")
            exit()
    if encrypt_type == '-r':
        os.system("cls")
        leng = input(Fore.MAGENTA + Style.BRIGHT + "Key length:  ")
        leng = int(leng)
        for i in file_list:
            generate_keys(leng, i, encrypt_type)
    else:
        pass

    


if __name__ == "__main__":
    main()
