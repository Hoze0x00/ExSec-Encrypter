import base64
import os
import tkinter
from tkinter import filedialog
import tkinter.messagebox
import customtkinter
from cryptography.fernet import Fernet
from win10toast import ToastNotifier

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x100")
        self.resizable(width=False, height=False)
        self.title("ExSec Decrypter")
        cwd = os.getcwd()
        cwd = cwd.replace("\\", "&")
        cwd = cwd.split("&")
        final_cwd = ""
        for x in cwd:
            if x == "ExSec-Decrypter":
                final_cwd = final_cwd + x + "\\"
                break
            else:
                final_cwd = final_cwd + x + "\\"
        self.iconbitmap(final_cwd + "Icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.button1 = customtkinter.CTkButton(text="Browse", command=self.browser)
        self.button1.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)
        self.passw = customtkinter.CTkEntry(master=None,
                                    width=120,
                                    placeholder_text="Password")
        self.passw.place(relx=0.1, rely=0.5, anchor=tkinter.W)
        self.passw1= customtkinter.CTkEntry(master=None,
                                    width=120,
                                    placeholder_text="Key")
        self.passw1.place(relx=0.1, rely=0.2, anchor=tkinter.W)
        self.button = customtkinter.CTkButton(text="Decrypt",
                                                border_width=1, 
                                                fg_color=None,
                                                command=self.start_decrypter)
        self.button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
        self.label_1 = customtkinter.CTkLabel(master=None,
                                        text="Files To Decrypted: -")
        self.label_1.place(relx=0.35, rely=0.8)
        self.file_list_to_dec = []


    def decrypt(self, filename):
        secret = self.passw1.get().encode('utf8')
        f = Fernet(secret)
        with open(filename, "rb") as file:
            file_data = file.read()
        decrypted_data  = f.decrypt(file_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
    def start_decrypter(self):
        usr = os.getlogin()
        file_open = open(f"C:\\Users\\{usr}\\AppData\Local\\Temp\\fn48fn39f8h984hfw94fh4fnoacn(HD)DN98dn8.txt", "r")
        for lines in file_open:
            lines = base64.b64decode(lines).decode('utf-8')
            print(self.passw.get() + "  " + lines)
            if self.passw.get() != lines:
                tkinter.messagebox.showerror('Auth Error', 'Password Incorrect!')
                exit(self.start_decrypter)
            else:
                for fils in self.file_list_to_dec:
                    self.decrypt(fils)
        toast = ToastNotifier()
        toast.show_toast(
            "Info",
            f"{str(self.length)} files Decrypted.",
            duration = 20,
            threaded = True,
        )
    
    def browser(self):
        file_path = filedialog.askopenfilenames()
        for files in file_path:
            self.file_list_to_dec.append(files)
        self.length = len(file_path)
        self.label_1.configure(text= "Files To Be Decrypted: " + str(self.length))
        self.label_1.update_idletasks()

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()