import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import secrets
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self) :
        mine = self.pte_mine.toPlainText()
        com = ""
        
        rnd = random()
        
        if rnd> 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else :
            com ="보"
            
        if com == "가위" and mine == "가위": result = "비김"
        if com == "가위" and mine == "바위": result = "이김"
        if com == "가위" and mine == "보": result = "패배"
        
        if com == "바위" and mine == "바위": result = "비김"
        if com == "바위" and mine == "가위": result = "패배"
        if com == "바위" and mine == "보": result = "이김"
        
        if com == "보" and mine == "보": result = "비김"
        if com == "보" and mine == "가위": result = "이김"
        if com == "보" and mine == "바위": result = "패배"
        
        self.pte_com.setPlainText(com)
        self.pte_result.setPlainText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()