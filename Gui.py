from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QTimer

import serial, time
from SpecialSerialPort import SpecialSerialPort
from DetectSerialPort import DetectSerialPort

class Gui(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.createInterface()
        self.show()

        self.detectSerialPort = DetectSerialPort()   ##create detect available COM




    def findCom(self):
        comInst = str(self.SerialPortLine.text())
        if(comInst == ""):
            self.LogLine.setText("Nothing to find.")
            return -1

        self.LogLine.setText("To find in COM instances: " + comInst)
        self.detectSerialPort.toFind = comInst
        comPort = self.detectSerialPort.detectPort()

        if (comPort == None ):
            self.LogLine.setText("Not found.")
        else:
            self.LogLine.setText("Found: " + str(comPort))

    def connectCom(self):
        self.LogLine.setText("Pressed connect COM")


    def disconnectCom(self):
        self.LogLine.setText("Pressed disconnect COM")

    def printLog(self):
        pass

    def printTemp(self):
        pass

    def printTempAvg(self):
        pass


    def createButtosn(self):
        self.findCOM = QPushButton("&Find", self)
        self.connectCOM = QPushButton("&Connect", self)
        self.disconnectCOM = QPushButton("&Disconnect", self)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.findCOM)
        self.buttonLayout.addWidget(self.connectCOM)
        self.buttonLayout.addWidget((self.disconnectCOM))

        #connect button with functions
        self.findCOM.clicked.connect(self.findCom)
        self.connectCOM.clicked.connect(self.connectCom)
        self.disconnectCOM.clicked.connect(self.disconnectCom)


        self.layOutPattern.addLayout(self.buttonLayout, 2, 0, 1, 1)
        self.setLayout(self.layOutPattern)

    def createLineEdit(self):
        #create line edit
        self.SerialPortLine = QLineEdit()
        self.TemperatureLine = QLineEdit()
        self.TempertureAvgLine = QLineEdit()
        self.LogLine = QLineEdit()

        #line settings
        #self.SerialPortLine.setReadOnly(True)
        self.TemperatureLine.setReadOnly(True)
        self.TempertureAvgLine.setReadOnly(True)
        self.LogLine.setReadOnly(True)

        #line tool tip
        self.SerialPortLine.setToolTip('Serial port information.')
        self.TemperatureLine.setToolTip('Tank CPU temperature.')
        self.TempertureAvgLabel.setToolTip('Average CPU temperature.')
        self.LogLine.setToolTip('Program logs.')

        #size
        self.LogLine.setMinimumSize(120,60)
        self.TemperatureLine.setMaximumSize(150, 20)
        self.TempertureAvgLine.setMaximumSize(150, 20)

        #aligment
        self.LogLine.setAlignment(Qt.AlignTop)
        self.TemperatureLine.setAlignment(Qt.AlignRight)
        self.TempertureAvgLine.setAlignment(Qt.AlignRight)

        self.layOutPattern.addWidget(self.SerialPortLine, 1, 0)
        self.layOutPattern.addWidget(self.TemperatureLine, 1, 4)
        self.layOutPattern.addWidget(self.TempertureAvgLine, 3, 4)
        self.layOutPattern.addWidget(self.LogLine, 5, 0, 1, 3)

        self.layOutPattern.setColumnMinimumWidth(4, 150)
        self.layOutPattern.setColumnMinimumWidth(0, 150)

        self.setLayout(self.layOutPattern)

    def createLabels(self):
        #lables
        self.SerialPortLabel = QLabel("Serial Port: ", self)
        self.TemperatureLabel = QLabel("CPU temperature: ", self)
        self.TempertureAvgLabel = QLabel("CPU average temperature", self)
        self.LogsLabel = QLabel("Logs: ", self)

        #aligment
        self.TemperatureLabel.setAlignment(Qt.AlignLeft)
        self.TempertureAvgLabel.setAlignment(Qt.AlignLeft)

        #connect labels to layout
        self.layOutPattern.addWidget(self.SerialPortLabel, 0, 0)
        self.layOutPattern.addWidget(self.TemperatureLabel, 0, 4)
        self.layOutPattern.addWidget(self.TempertureAvgLabel, 2, 4)
        self.layOutPattern.addWidget(self.LogsLabel, 4, 0)


        self.setLayout(self.layOutPattern)

    def createInterface(self):
        self.layOutPattern = QGridLayout()

        self.createLabels()
        self.createLineEdit()
        self.createButtosn()

        #windows settings
        self.setGeometry(200, 200, 600, 200)
        self.setWindowTitle("Tank GUI")
        self.setWindowIcon(QIcon('tank_icon.png'))




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Gui()
    sys.exit(app.exec_())