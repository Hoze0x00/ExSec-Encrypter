import base64
import platform
import time
import tkinter
from tkinter import Button, Label, Tk, Toplevel, filedialog
import tkinter.messagebox
import customtkinter
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from win10toast import ToastNotifier

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
class App(customtkinter.CTk):
    
    WIDTH = 1000
    HEIGHT = 520
    def __init__(self):
        super().__init__()
        self.title("ExSec Encrypter")
        cwd = os.getcwd()
        cwd = cwd.replace("\\", "&")
        cwd = cwd.split("&")
        final_cwd = ""
        for x in cwd:
            if x == "ExSec-Encrypter":
                final_cwd = final_cwd + x + "\\"
                break
            else:
                final_cwd = final_cwd + x + "\\"
        self.iconbitmap(final_cwd + "Icon.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="File Encrypter",
                                              text_font=("Roboto Medium", -19))
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")


        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")


        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1) 
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=None,
                                                   height=400,
                                                   corner_radius=10,
                                                   fg_color=("white", "black"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=10, pady=15)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Files to be Encrypted:",
                                                        fg_color="black")
        self.label_radio_group.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=70, sticky="we")
        self.radio_var = tkinter.IntVar(value=0)
        self.button_x = customtkinter.CTkButton(master=self.frame_right,
                                                text="Browse Files",
                                                border_width=1,
                                                fg_color=None,
                                                command=self.browser)
        self.button_x.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")


        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Encrypt!",
                                                border_width=2,
                                                fg_color=None,
                                                command=self.enc)
        self.button_5.grid(row=8, column=2, columnspan=2, pady=20, padx=20, sticky="we")
        self.passw = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Password")
        self.passw.grid(row=9, column=0, columnspan=2, pady=20, padx=20, sticky="we")


        self.optionmenu_1.set("Dark")
    def browser(self):
        file_path = filedialog.askopenfilenames()
        file_list = []
        for files in file_path:
            file_list.append(files)
        new_text = ""
        for file_list_files in file_list:
            new_text = new_text + file_list_files + '\n'
        self.label_info_1.configure(text= new_text)
        self.label_info_1.update_idletasks()
        self.files = file_list
        

    def enc(self):
        def main_enc(filename, key):
            f = Fernet(key)
            with open(filename, "rb") as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(filename, "wb") as file:
                try:
                    file.write(encrypted_data)
                except PermissionError:
                    tkinter.messagebox.showerror('Permission Error', "Error: It seems like you don't have privileges high enough to encrypt this file. Maybe run as Admin? ;(")
        if len(self.files) < 1:
            tkinter.messagebox.showerror('File Error', 'Error: No files selected!')
            return None
        original_passwd = self.passw.get()
        if len(original_passwd) < 4:
            tkinter.messagebox.showerror('Password Error', 'Error: Password minium length is 4!')
            return None
        system = platform.system()
        username = os.getlogin()
        if system == "Windows":
            check = os.path.exists(f"C:\\Users\\{username}\\AppData\\Local\\Temp")
            if check == True:
                os.system(f"type > nul C:\\Users\\{username}\\AppData\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt")
                open_temp = open(f"C:\\Users\\{username}\\AppData\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt", "wb")
                passwrd = original_passwd
                passwrd = base64.b64encode(passwrd.encode('utf-8'))
                open_temp.write(passwrd)
        elif system != "Windows":
            exit()
        passwd = original_passwd.encode("utf-8")
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
        

        secret_key = secret_in_string
        secret_password = original_passwd
        for files in self.files:
            main_enc(files, key)
        toast = ToastNotifier()
        toast.show_toast(
            "Info",
            "All files encrypted successfully.",
            duration = 20,
            threaded = True,
            )
        time.sleep(0.5)
        def copy1():
            copy1_text = Tk()
            copy1_text.withdraw()
            copy1_text.clipboard_clear()
            copy1_text.clipboard_append(secret_key)
            copy1_text.destroy()
        def copy2():
            copy2_text = Tk()
            copy2_text.withdraw()
            copy2_text.clipboard_clear()
            copy2_text.clipboard_append(secret_password)
            copy2_text.destroy()
        top= Toplevel(app)
        top.geometry("600x58")
        top.resizable(width=False, height=False)
        top.title("Credentials")
        Label(top, text= "Key: " + secret_key, bg="black", fg="green", font=("COPPERPLATE GOTHIC BOLD", 12)).place(x=2,y=0)
        Label(top, text= "Password: " + secret_password, bg="black", fg="green", font=("COPPERPLATE GOTHIC BOLD", 15)).place(x=2,y=26)
        Button(top, text= "Copy!", command=copy2).place(x=400,y=26)
        Button(top, text= "Copy!", command=copy1).place(x=540,y=0)
        top['background']='black'
        
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode == "Light":
            self.label_radio_group.configure(fg_color="white")
        if new_appearance_mode == "Dark":
            self.label_radio_group.configure(fg_color="black")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()