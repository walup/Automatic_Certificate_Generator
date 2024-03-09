
from Utilities import ExcelHandler
from Utilities import WordEditor
from Utilities import Text2QR
from ProgressBarWindow import ProgressBar
import time

class WordBuilder:

    def __init__(self, wordPath, excelPath, outputPath):
        self.wordPath = wordPath
        self.excelPath = excelPath
        self.outputPath = outputPath
        self.QR_WIDTH = 10
        self.QR_HEIGHT = 10

    def generateCertificates(self, master):
        self.excelHandler = ExcelHandler(self.excelPath)
        tags = self.excelHandler.getSheetFieldNames()
        nTags = len(tags)

        limitChars = 10

        nEntries = self.excelHandler.getNEntries()
        progressBar = ProgressBar(master, "Generando certificados")
        for p in range(0,nEntries):
            self.wordDocument =WordEditor(self.wordPath)
            progressBar.setProgressBar((p+1)/nEntries)
            dataForQR = []
            for i in range(0,nTags):
                tag = tags[i]
                tagData = str(self.excelHandler.getSheetField(tag)[p]).split(";")
                dataForQR.append(tagData)
                if(len(tagData) == 1):
                    self.wordDocument.substitutePattern("<<" + tag + ">>", tagData[0])
                else:
                    strData = ""
                    horizontal = True
                    for j in range(0,len(tagData)):
                        if(len(tagData[j]) > limitChars):
                            horizontal = False
                            break
                
                    for j in range(0,len(tagData)):

                        if(horizontal and j <len(tagData) - 1):
                            strData = strData + tagData[j] + ","
                        elif(horizontal and j == len(tagData) - 1):
                            strData = strData + tagData[j]
                        elif(not horizontal):
                            strData = strData + "-"+tagData[j] + "\n"
                
                    self.wordDocument.substitutePattern("<<" + tag + ">>", strData)
            

        
            #Generate the qr 
                
            refinedTags = []
            for i in range(0,len(tags)):
                refinedTags.append(tags[i][0].upper() + tags[i][1:].lower())
        
            text2QR = Text2QR(refinedTags, dataForQR)
            qrPath = "temp_images/temp.png"
            text2QR.saveQR(qrPath)
            time.sleep(2)
            self.wordDocument.insertImage(qrPath, 7, 7)
            outputWordPath = self.outputPath + "/" + str(p) + ".docx"
            outputPDFPath = self.outputPath + "/" + str(p) + ".pdf"
            self.wordDocument.saveAsPDF(outputWordPath, outputPDFPath)

                

                    

                    









    


