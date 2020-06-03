from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtWidgets, uic
from functools import partial
import os, sys, threading, atexit

# image lists
# path
image_paths = []
# name
image_names = []

last_clicked = 0
class mainwindowUI(QMainWindow):
    def __init__(self, parent = None):
        super(mainwindowUI, self).__init__(parent)
        uic.loadUi('Scripts/GUI/Hutterite_Bookshelf_GUI/mainwindow.ui', self)
        self.load_ui_objects()
        keyPressed = QtCore.pyqtSignal(int)
        self.show()
    def load_ui_objects(self):
        # checkboxes
        self.checkboxSortText = self.findChild(QCheckBox, 'checkBox')
        self.checkboxOrginizeText = self.findChild(QCheckBox, 'checkBox_2')
        self.checkboxCorrectText = self.findChild(QCheckBox, 'checkBox_3')
        self.checkboxGenerateList = self.findChild(QCheckBox, 'checkBox_4')

        # lineedits
        self.lineeditDirectoryListGenerator = self.findChild(QLineEdit, 'lineEdit_4')
        self.lineeditFileName = self.findChild(QLineEdit, 'txtFileName')
        
        # buttons
        self.buttonStart = self.findChild(QPushButton, 'btnStart')
        # self.buttonStart.clicked.connect(self.start)
        self.buttonSelectFiles = self.findChild(QPushButton, 'btnSelectFiles')
        self.buttonSelectFiles.clicked.connect(self.selectFiles)
        
        # progressbar
        self.progressBar = self.findChild(QProgressBar, 'progressBar')
        
        # listwidget
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.listWidget.itemClicked.connect(self.lastClicked)
        self.listWidget.itemDoubleClicked.connect(self.Clicked)

    def selectFiles(self):
        global image_names, image_paths
        options = QFileDialog.Options()
        image_paths, _ = QFileDialog.getOpenFileNames(self,"Images","Images","Image Files (*.jpg, *.png)", options=options)
        # print(fileName)
        image_names.clear()
        for i, j in enumerate(image_paths):
            j = j.split('/')
            j = j[-1]
            image_names.append(j)
            self.listWidget.addItem(f'{str(i+1)}. {j}')
    def Clicked(self,item):
        QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
    def lastClicked(self,item):
        global last_clicked
        last_clicked = item.text()
        last_clicked = last_clicked.split('.')
        last_clicked = int(last_clicked[0])
    # def start(self):
        # for i, j in enumerate(image_paths):
            
    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Delete:
                # self.emit(QtCore.SIGNAL('MYSIGNAL'))
                self.deleteSelected(last_clicked)
    def deleteSelected(self, index):
        global image_names, image_paths
        index = index - 1
        image_paths.pop(index)
        image_names.clear()
        self.listWidget.clear()
        for i, j in enumerate(image_paths):
            j = j.split('/')
            j = j[-1]
            image_names.append(j)
            self.listWidget.addItem(f'{str(i+1)}. {j}')
def exit_handler(): sys.exit()
if __name__ == '__main__':
    atexit.register(exit_handler)
    
    app = QApplication(sys.argv)
    window = mainwindowUI()
    
    app.exec_()