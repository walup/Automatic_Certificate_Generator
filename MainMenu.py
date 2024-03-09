import customtkinter
import tkinter as Tk

class MainMenu(Tk.Menu):

    def __init__(self, master):

        super().__init__(master)

        self.INSTRUCTIONS_LABEL = "Instrucciones"
        self.INFORMATION_LABEL = "Información"
        self.EXIT_LABEL = "Cerrar Aplicación"

        #Info menu
        infoMenu = Tk.Menu(self, tearoff = 0)
        infoMenu.add_command(label = self.INSTRUCTIONS_LABEL, command = lambda:self.displayInstructions())
        infoMenu.add_separator()
        infoMenu.add_command(label = self.EXIT_LABEL, command = self.master.destroy)

        self.font = customtkinter.CTkFont(family = "Helvetica'",size = 12)



        self.add_cascade(label = self.INFORMATION_LABEL, menu = infoMenu)

    

    def displayInstructions(self):
        file = open("assets/instructions.txt")
        stringFile = file.read()

        instructionWindow = customtkinter.CTkToplevel(self.master)
        instructionWindow.title(self.INSTRUCTIONS_LABEL)
        instructionWindow.geometry("640x360")
        instructionText = customtkinter.CTkTextbox(master = instructionWindow, width = 600, height = 300)
        instructionText.pack(pady = 10, padx = 20)
        instructionText.insert('0.0', stringFile)
        instructionText.configure(state = "disabled")


        print(stringFile)

    def doNothing(self):
        print("Doing nothing")