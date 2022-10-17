from fernet import Fernet
from colorama import Fore, Style, init
import sys
import os
import base64

init()
usr = os.getlogin()
try:
    file_open = open(f"C:\\Users\\{usr}\\AppData\\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt", "r")
    #If your here to check why error below is occuring, check if the file above exists. Or if not, create a file with the password on it on line 1. And replace path above with the new path/file :)
except:
    print("Password File Not found, create one by running the encrypter!")
    exit()


def decrypt(filename, keys, secret):
    passwrd = sys.argv[2]
    for lines in file_open:
        lines = base64.b64decode(lines).decode('utf-8')
        if passwrd != lines:
            os.system('cls')
            print(Fore.RED + Style.BRIGHT + "Wrong password: ", keys)
            exit()
    else:
        pass
    secret = secret.encode('utf8')
    f = Fernet(secret)
    with open(filename, "rb") as file:
        file_data = file.read()
    decrypted_data  = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    os.system('cls')
    print(Fore.CYAN + Style.BRIGHT + f"---->  {filename} is now decrypted!")

def main():
    try:
        checker = os.path.exists(sys.argv[1])
        if checker == True:
            pass
        if checker == False:
            print(Fore.RED + Style.BRIGHT + f"[-] No such file or directory: {sys.argv[1]}")
            exit()
        try:
            decrypt(sys.argv[1], sys.argv[2], sys.argv[3])
        except IndexError:
            print(Fore.RED + Style.BRIGHT + "[-] Not enough keys found in arguments...")
            print( f"Usage: {sys.argv[0]} <filename> <password> <key>")
            exit()
    except IndexError:
        print(Fore.RED + Style.BRIGHT + f"Usage: {sys.argv[0]} <filename> <password> <key>")

if __name__ == "__main__":
    main()