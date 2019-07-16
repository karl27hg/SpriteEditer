import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiDirPath, _ = os.path.split(__file__)
mainWinUiPath = os.path.join(uiDirPath, "../ui/mainWin.ui")
ui_mainWin = uic.loadUiType(mainWinUiPath)[0]
class MainWin(QMainWindow, ui_mainWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    app.exec_()
