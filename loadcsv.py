# fsf_2019_screening_task2
#Project on plotting given values from a csv file using pyqt
#This will allow us to load a csv file
#Defaultly it will take tab spaces as delimeter.

import csv, codecs 
import os
 
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile
#importing pyqt5 libraries

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = ""
        self.fname = "plot"
        self.model =  QtGui.QStandardItemModel(self)
 
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setStyleSheet(stylesheet(self))
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setShowGrid(True)
        self.tableView.setGeometry(50, 50, 780, 645)
        self.model.dataChanged.connect(self.finishedEdit)
 
        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load CSV")
        self.pushButtonLoad.clicked.connect(self.loadCsv)
        self.pushButtonLoad.setFixedWidth(80)
        self.pushButtonLoad.setStyleSheet(stylesheet(self))
    
    def finishedEdit(self):
        self.tableView.resizeColumnsToContents()
    
    def loadCsv(self, fileName):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open CSV",
               (QtCore.QDir.homePath()), "CSV (*.csv *.tsv)")
 
        if fileName:
            print(fileName)
            ff = open(fileName, 'r')
            mytext = ff.read()
            ff.close()
            f = open(fileName, 'r')
            with f:
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                print(self.fname)
                self.setWindowTitle(self.fname)
                if mytext.count(';') <= mytext.count('\t'):
                    reader = csv.reader(f, delimiter = '\t')
                    self.model.clear()
                    for row in reader:    
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()
                else:
                    reader = csv.reader(f, delimiter = ';')
                    self.model.clear()
                    for row in reader:    
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.tableView.resizeColumnsToContents()
def stylesheet(self):
    return """
       QTableView
       {
border: 1px solid grey;
border-radius: 0px;
font-size: 12px;
        background-color: #f8f8f8;
selection-color: white;
selection-background-color: #00ED56;
       }
 
QTableView QTableCornerButton::section {
    background: #D6D1D1;
    border: 1px outset black;
}
 
QPushButton
{
font-size: 11px;
border: 1px inset grey;
height: 24px;
width: 80px;
color: black;
background-color: #e8e8e8;
background-position: bottom-left;
} 
 
QPushButton::hover
{
border: 2px inset goldenrod;
font-weight: bold;
color: #e8e8e8;
background-color: green;
} 
"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')
    main = MyWindow('')
    main.setMinimumSize(500, 300)
    main.setGeometry(0,0,800,700)
    main.setWindowTitle("Plotter")
    main.show()
    sys.exit(app.exec_())
