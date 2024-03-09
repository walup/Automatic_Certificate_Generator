import customtkinter

class ProgressBar:

    def __init__(self, master, title):

        self.progressBarWindow = customtkinter.CTkToplevel(master)
        self.progressBarWindow.title(title)
        self.progressBarWindow.geometry("300x250")
        self.progressBar = customtkinter.CTkProgressBar(self.progressBarWindow, orientation = "horizontal")
        self.progressBar.pack(padx = 10, pady = 10)
        self.progressBar.set(0)
        self.root = master
    
    def setProgressBar(self, value):
        self.progressBar.set(value)
        self.root.update()

        if(value == 1.0):
            self.progressBarWindow.destroy()


