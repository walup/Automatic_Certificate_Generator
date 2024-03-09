import customtkinter
from PIL import Image
from WordBuilder import WordBuilder

class MainPageFrame(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        # Frame final parameters
        self.FRAME_WIDTH = 400
        self.FRAME_HEIGHT = 200

        super().__init__(master, width = self.FRAME_WIDTH, height = self.FRAME_HEIGHT)
        
        self.SEARCH_DIR_LIGHT_IMAGE_PATH = "assets/search_dir_light.png"
        self.SEARCH_DIR_DARK_IMAGE_PATH = "assets/search_dir_dark.png"

        self.WORD_TEMPLATE_LABEL = "Plantilla de Word"
        self.EXCEL_TABLE_LABEL = "Tabla de Excel"
        self.GENERATE_CERTIFICATES_LABEL = "Generar Constancias"
        self.OUTPUT_PATH_LABEL = "Directorio de Salida"
        self.SEARCH_BUTTON_PLACEHOLDER_TEXT = "Buscar"
        self.TEXT_FIELD_WIDTH = 100
        self.TEXT_FIELD_HEIGHT = 5
        self.IMAGE_ICON_WIDTH = 30
        self.IMAGE_ICON_HEIGHT = 30
        self.PAD_X = 5
        self.PAD_Y = 10

        self.defaultFont = customtkinter.CTkFont(family = "Helvetica'",size = 12)

        #Labels
        self.wordTemplateLabel = customtkinter.CTkLabel(master = self, text = self.WORD_TEMPLATE_LABEL, font = self.defaultFont)
        self.wordTemplateLabel.grid(row = 0, column = 0,padx = self.PAD_X, pady = self.PAD_Y)
        self.excelTableLabel = customtkinter.CTkLabel(master = self, text = self.EXCEL_TABLE_LABEL, font = self.defaultFont)
        self.excelTableLabel.grid(row = 1, column = 0, padx = self.PAD_X, pady = self.PAD_Y)
        self.outputPathLabel = customtkinter.CTkLabel(master = self, text = self.OUTPUT_PATH_LABEL, font = self.defaultFont)
        self.outputPathLabel.grid(row = 2, column = 0, padx = self.PAD_X, pady = self.PAD_Y)


        #Text boxes
        self.wordPathText = customtkinter.CTkTextbox(master = self, width = self.TEXT_FIELD_WIDTH, height = self.TEXT_FIELD_HEIGHT)
        self.excelPathText = customtkinter.CTkTextbox(master = self, width = self.TEXT_FIELD_WIDTH, height = self.TEXT_FIELD_HEIGHT)
        self.outputPathText = customtkinter.CTkTextbox(master = self, width = self.TEXT_FIELD_WIDTH, height = self.TEXT_FIELD_HEIGHT)
        self.wordPathText.grid(row = 0,column = 1, padx = self.PAD_X, pady = self.PAD_Y)
        self.excelPathText.grid(row = 1, column = 1, padx = self.PAD_X, pady = self.PAD_Y)
        self.outputPathText.grid(row = 2, column = 1, padx = self.PAD_X, pady = self.PAD_Y)

        #Buttons
        self.searchDirImage = customtkinter.CTkImage(light_image = Image.open(self.SEARCH_DIR_LIGHT_IMAGE_PATH), dark_image = Image.open(self.SEARCH_DIR_LIGHT_IMAGE_PATH), size = (self.IMAGE_ICON_WIDTH, self.IMAGE_ICON_HEIGHT))
        self.searchPathButtonWord = customtkinter.CTkButton(master =self, text = self.SEARCH_BUTTON_PLACEHOLDER_TEXT, font = self.defaultFont, image = self.searchDirImage, command=lambda: self.searchDirectory(self.wordPathText))
        self.searchPathButtonExcel = customtkinter.CTkButton(master = self, text = self.SEARCH_BUTTON_PLACEHOLDER_TEXT, font = self.defaultFont, image = self.searchDirImage, command = lambda:self.searchDirectory(self.excelPathText))
        self.searchPathButtonOutput = customtkinter.CTkButton(master = self, text = self.SEARCH_BUTTON_PLACEHOLDER_TEXT, font = self.defaultFont, image = self.searchDirImage, command = lambda:self.searchDir2(self.outputPathText))
        self.generateButton = customtkinter.CTkButton(master = self, text = self.GENERATE_CERTIFICATES_LABEL, font = self.defaultFont, command = lambda:self.generateCertificates())
        self.searchPathButtonWord.grid(row = 0, column = 2, padx = self.PAD_X, pady = self.PAD_Y)
        self.searchPathButtonExcel.grid(row = 1, column = 2, padx = self.PAD_X, pady = self.PAD_Y)
        self.searchPathButtonOutput.grid(row = 2, column = 2, padx = self.PAD_X, pady = self.PAD_Y)
        self.generateButton.grid(row = 3, column = 0, columnspan = 3, padx = self.PAD_X, pady = self.PAD_Y)

    def generateCertificates(self):
        excelPath = self.excelPathText.get("1.0", 'end-1c')
        wordPath = self.wordPathText.get("1.0", 'end-1c')
        outputPath = self.outputPathText.get("1.0", 'end-1c')

        wordBuilder = WordBuilder(wordPath, excelPath, outputPath)

        wordBuilder.generateCertificates(self.master)


    def searchDirectory(self, textBox):
        dirName = "Directorio no especificado"
        dirName = customtkinter.filedialog.askopenfilename()
        textBox.delete("0.0", "end")
        textBox.insert("0.0", dirName)

    def searchDir2(self, textBox):
        dirName = "Directorio no especificado"
        dirName = customtkinter.filedialog.askdirectory()
        textBox.delete("0.0", "end")
        textBox.insert("0.0", dirName)

    



        



        






