import customtkinter
from tkinter import *
from MainPageFrame import MainPageFrame
from MainMenu import MainMenu

class CertificateApp:


    def __init__(self):
        self.TITLE = "Generador de certificados QR"
        self.WINDOW_WIDTH = 420
        self.WINDOW_HEIGHT = 250
        self.WINDOW_STRING = str(self.WINDOW_WIDTH)+"x"+str(self.WINDOW_HEIGHT)
        #Apariencia de la ventana
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        root.title(self.TITLE)
        root.geometry(self.WINDOW_STRING)

        mainFrame = MainPageFrame(root)
        mainFrame.pack(side = TOP)

        mainMenu = MainMenu(root)

        root.config(menu = mainMenu)

        root.mainloop()




CertificateApp()
