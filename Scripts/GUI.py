from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtWidgets, uic, QtCore, QtWidgets, QtPrintSupport, QtGui
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from functools import partial
import os, sys, threading, atexit
import Auto_Correct_Text as correctText
import Auto_Orginize_Text as orginizeText
import Auto_Read_Page as readText
import Auto_Sort_Text as sortText
import List_Generator as listGen
import time
import pytesseract, os, glob, codecs, subprocess, platform
try: from PIL import Image
except ImportError: import Image
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
        for i, j in enumerate(self.files[self.startNum:]):
            time.sleep(1)
            path = j
            # print(path)
            if platform.system() == 'Windows': 
                pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
                s = pytesseract.image_to_string(path)
                with codecs.open(self.filename, 'a', encoding='utf-8', errors="ignore") as f: f.write(s + '\n')
            elif platform.system() == "Linux": 
                text = os.popen(f'tesseract \"{path}\" stdout').read()
                with codecs.open(self.filename, 'a', encoding='utf-8', errors="ignore") as f: f.write(text + '\n')
            self.converted.emit(f'Completed {j} - {i+1}/{len(self.files)-self.startNum}')
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
        self.txtOutputFilename = '' 
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
                fileLoc = os.path.dirname(os.path.abspath(__file__)) + '/Extracted'
                temp_filename = self.txtOutputFilename
                temp_filename.split('/')
                temp_filename = temp_filename[-1]
                if self.checkboxCorrectText.isChecked(): 
                    self.progressBar.setFormat(f' Correcting {temp_filename}.')
                    correctText.replace_text(self.txtOutputFilename)
                if self.checkboxOrginizeText.isChecked(): 
                    self.progressBar.setFormat(f' Orginizing {temp_filename}..')
                    orginizeText.orginize_text(self.txtOutputFilename)
                if self.checkboxSortText.isChecked(): 
                    self.progressBar.setFormat(f' Sorting {temp_filename}...')
                    sortText.extract_text(fileLoc, self.txtOutputFilename)
                if self.checkboxGenerateList.isChecked(): 
                    self.progressBar.setFormat(f' Generating list for {temp_filename}....')
                    listGen.list_gen(fileLoc)
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
        temp = item.text()
        temp = temp.split('.')
        index = temp[0]
        path = self.image_paths[int(index)-1]
        print(path)
        self.openImage(path)
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
        self.txtOutputFilename = os.path.dirname(os.path.abspath(__file__)) + '/' + new_filename + '.txt'
        print(self.txtOutputFilename)
        self.start_conversion(self.image_paths, self.txtOutputFilename, 0)
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
    def openImage(self, path):
        self.vi = view_image(path)
        self.vi.show()
        # self.close()
class view_image(QMainWindow):
    def __init__(self, directory_to_open,):
        super(view_image, self).__init__()
        self.viewer = PhotoViewer(self)
        self.image_to_open = directory_to_open
        directory_to_open = directory_to_open.replace('\\','/')

        self.printer = QPrinter()
        self.setWindowTitle(directory_to_open)
        self.createActions()
        self.createMenus()
        # self.resize(width, height)

        screen = app.primaryScreen()
        rect = screen.availableGeometry()

        self.setGeometry(0, 0, rect.width(), rect.height())
        self.viewer.photoClicked.connect(self.photoClicked)

        # Arrange layout
        self.VBlayout = QVBoxLayout(self)
        self.VBlayout.addWidget(self.viewer)
        self.HBlayout = QHBoxLayout(self)
        self.HBlayout.setAlignment(Qt.AlignLeft)
        self.VBlayout.addLayout(self.HBlayout)
        self.setCentralWidget(self.viewer)
        self.loadImage() 
        self.viewer.fitInView(True)
        # self.setCentralWidget(VBlayout)
        # self.menuBar = QMenuBar(self)
    def createActions(self):
        self.printAct = QAction("&Print...", self, shortcut="Ctrl+P", enabled=True, triggered=self.print_)
    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.printAct)
        self.menuBar().addMenu(self.fileMenu)
    def print_(self):
        dialog = QtPrintSupport.QPrintPreviewDialog() # PyQt5
        # dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()
    def handlePaintRequest(self, printer):
        self.viewer.render(QPainter(printer))
    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.editor.document().print_(dialog.printer())
    def loadImage(self):
        self.viewer.setPhoto(QPixmap(self.image_to_open))
        self.showMaximized()
    def pixInfo(self):
        self.viewer.toggleDragMode()
    def photoClicked(self, pos):
        if self.viewer.dragMode()  == QGraphicsView.NoDrag:
            self.editPixInfo.setText('%d, %d' % (pos.x(), pos.y()))
    def closeEvent(self, event):
        self.mm = mainwindowUI()
        self.mm.show()
        self.close()
class PhotoViewer(QGraphicsView):
    photoClicked = pyqtSignal(QPoint)
    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 100
        self._empty = True
        self._scene = QGraphicsScene(self)
        self._photo = QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        self.setFrameShape(QFrame.NoFrame)
    def hasPhoto(self):
        return not self._empty
    def fitInView(self, scale=True):
        rect = QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0
    def setPhoto(self, pixmap=None):
        self._zoom = 100
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())
        self.fitInView()
    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
    def toggleDragMode(self):
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            self.setDragMode(QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QGraphicsView.ScrollHandDrag)
    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
        super(PhotoViewer, self).mousePressEvent(event)
def exit_handler(): sys.exit()
if __name__ == '__main__':
    atexit.register(exit_handler)
    app = QApplication(sys.argv)
    window = mainwindowUI()
    app.exec_()