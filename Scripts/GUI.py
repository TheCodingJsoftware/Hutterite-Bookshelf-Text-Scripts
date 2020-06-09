from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtWidgets, uic
from functools import partial
import os, sys, threading, atexit
import Auto_Correct_Text as correctText
import Auto_Orginize_Text as orginizeText
import Auto_Read_Page as readText
import Auto_Sort_Text as sortText
import List_Generator as listGen
import time
# image lists
# path
# name
class ConvertThread(QThread):  
    converted = pyqtSignal(object)
    def __init__(self, l):
        QThread.__init__(self)
        self.files = l[0]
        self.filename = l[1]
        self.startNum = l[2]
    def run(self):
        # j = self.file
        self.converted.emit(f'Starting {self.files[0]} - 1/{len(self.files)-self.startNum}')
        # time.sleep(1)
        
        # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

        for i, j in enumerate(self.files[self.startNum:]):
            path = j
            # print(path)
            # s = pytesseract.image_to_string(path)
            # with codecs.open(filename, 'a', encoding='utf-8', errors="ignore") as f:
                # f.write(s + '\n')
            # text_file = codecs.open('All Songs test 1.txt',
            #                         mode='a', encoding='utf-8', errors="ignore")
            # text_file.write(s + '\n')
            # text_file.close()
            self.converted.emit(f'Completed {j} - {i+1}/{len(self.files)-self.startNum}')
        print('done')
        self.converted.emit('Finished!')
        time.sleep(1)
        self.converted.emit('')
class mainwindowUI(QMainWindow):
    def __init__(self, parent = None):
        super(mainwindowUI, self).__init__(parent)
        uic.loadUi('Scripts/GUI/Hutterite_Bookshelf_GUI/mainwindow.ui', self)
        self.setStyleSheet(open("Scripts/GUI/style.qss", "r").read())
        self.load_variables()
        self.load_ui_objects()
        keyPressed = QtCore.pyqtSignal(int)
        self.show()
    def load_variables(self):
        self.image_paths = []
        self.image_names = []
        self.last_clicked = 0
        self.fileNameRegex = QRegExp('^(?!\\.)(?!com[0-9]$)(?!con$)(?!lpt[0-9]$)(?!nul$)(?!prn$)[^\\|\\*\?\\:<>\/$"]*[^\\.\\|\\*\\?\\\:<>\/$"]+$')
    def load_ui_objects(self):
        # checkboxes
        self.checkboxSortText = self.findChild(QCheckBox, 'checkBox')
        self.checkboxOrginizeText = self.findChild(QCheckBox, 'checkBox_2')
        self.checkboxCorrectText = self.findChild(QCheckBox, 'checkBox_3')
        self.checkboxGenerateList = self.findChild(QCheckBox, 'checkBox_4')

        # lineedits
        self.lineeditDirectoryListGenerator = self.findChild(QLineEdit, 'lineEdit_4')

        self.lineeditFileName = self.findChild(QLineEdit, 'txtFileName')
        self.lineeditFileName.textChanged.connect(self.checkIfFileNameValid)
        input_validator = QRegExpValidator(self.fileNameRegex, self.lineeditFileName)
        self.lineeditFileName.setValidator(input_validator)
        
        # buttons
        self.buttonStart = self.findChild(QPushButton, 'btnStart')
        self.buttonStart.setEnabled(False)
        self.buttonStart.clicked.connect(self.btnstart)

        self.buttonSelectFiles = self.findChild(QPushButton, 'btnSelectFiles')
        self.buttonSelectFiles.clicked.connect(self.selectFiles)
        
        self.buttonClear = self.findChild(QPushButton, 'btnClear')
        self.buttonClear.clicked.connect(self.clearListWidget)
        
        # progressbar
        self.progressBar = self.findChild(QProgressBar, 'progressBar')
        self.progressBar.setHidden(True)
        
        # listwidget
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.listWidget.itemClicked.connect(self.lastClicked)
        self.listWidget.itemDoubleClicked.connect(self.Clicked)
    def start_conversion(self, files, filename, startnum):
        self.threads = []
        converter = ConvertThread([files, filename, startnum])
        converter.converted.connect(self.on_data_ready)
        self.threads.append(converter)
        converter.start()
        print('starting')
    def on_data_ready(self, text):
        try:
            # self.lblState.setHidden(False)
            self.progressBar.setHidden(False)
            # self.lblState.setText(f"{text}")
            if not text == 'Finished!':
                if not text == '':
                    print(text)
                    currentNum = text.split(' - ')
                    currentNum = currentNum[-1].split('/')
                    currentNum = int(currentNum[0])
                    
                    maxnum = text.split('/')
                    maxnum = int(maxnum[-1])
                    # print(maxnum)
                    
                    self.progressBar.setValue(currentNum)
                    self.progressBar.setMaximum(maxnum)
            self.progressBar.setFormat(' ' + text)
            if text == '': 
                # self.clearLayout(self.gridLayoutItems)
                # self.reloadListUI('')
                self.progressBar.setHidden(True)
        except Exception as e:
            print(e)
    def selectFiles(self):
        options = QFileDialog.Options()
        image_paths, _ = QFileDialog.getOpenFileNames(self,"Images","Images","Image Files (*.jpg, *.png)", options=options)
        if image_paths:
            self.image_paths = image_paths
            for i, j in enumerate(self.image_paths):
                j = j.split('/')
                j = j[-1]
                self.image_names.append(j)
                self.listWidget.addItem(f'{str(i+1)}. {j}')
        self.checkIfFileNameValid()
    def checkIfFileNameValid(self):
        if len(self.image_paths) >= 1 and self.lineeditFileName.text() != '': self.buttonStart.setEnabled(True)
        else: self.buttonStart.setEnabled(False)
    def Clicked(self,item):
        QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
    def clearListWidget(self):
        self.image_names.clear()
        self.image_paths.clear()
        self.listWidget.clear()
        self.checkIfFileNameValid()   
    def lastClicked(self,item):
        self.last_clicked = item.text()
        self.last_clicked = self.last_clicked.split('.')
        self.last_clicked = int(self.last_clicked[0])
    def btnstart(self):
        new_filename = self.lineeditFileName.text().replace('.txt', '')
        self.start_conversion(self.image_paths, new_filename, 0)
    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_Delete:
                # self.emit(QtCore.SIGNAL('MYSIGNAL'))
                self.deleteSelected(self.last_clicked)
    def deleteSelected(self, index):
        index = index - 1
        self.image_paths.pop(index)
        self.image_names.clear()
        self.listWidget.clear()
        for i, j in enumerate(self.image_paths):
            j = j.split('/')
            j = j[-1]
            self.image_names.append(j)
            self.listWidget.addItem(f'{str(i+1)}. {j}')
        self.checkIfFileNameValid()
def exit_handler(): sys.exit()
if __name__ == '__main__':
    atexit.register(exit_handler)
    
    app = QApplication(sys.argv)
    window = mainwindowUI()
    
    app.exec_()