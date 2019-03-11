#This code is much similar to the previous one. And it enables us to save the file.

import csv, codecs 
import os
 
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile
 
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
 
        self.pushButtonWrite = QtWidgets.QPushButton(self)
        self.pushButtonWrite.setText("Save CSV")
        self.pushButtonWrite.clicked.connect(self.writeCsv)
        self.pushButtonWrite.setFixedWidth(80)
        self.pushButtonWrite.setStyleSheet(stylesheet(self))
        
    def finishedEdit(self):
        self.tableView.resizeColumnsToContents()
    
    def writeCsv(self, fileName):
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                myitem = self.model.item(row,column)
                if myitem is None:
                    item = QtGui.QStandardItem("")
                    self.model.setItem(row, column, item)
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", 
                       (QtCore.QDir.homePath() + "/" + self.fname + ".csv"),"CSV Files (*.csv)")
        if fileName:
            print(fileName)
            f = open(fileName, 'w')
            with f:
                writer = csv.writer(f, delimiter = '\t')
                for rowNumber in range(self.model.rowCount()):
                    fields = [self.model.data(self.model.index(rowNumber, columnNumber),
                                         QtCore.Qt.DisplayRole)
                    for columnNumber in range(self.model.columnCount())]
                    writer.writerow(fields)
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                self.setWindowTitle(self.fname)
 
 
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
    main.setMinimumSize(300, 300)
    main.setGeometry(0,0,800,700)
    main.setWindowTitle("Plotter")
    main.show()
    sys.exit(app.exec_())
                                        
