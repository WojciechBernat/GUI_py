from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Gui(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.createInterface()
        self.show()

    def createLineEdit(self):
        #create line edit
        self.SerialPortLine = QLineEdit()
        self.TemperatureLine = QLineEdit()
        ## Here is a place for add ne label
        ##
        self.LogLine = QLineEdit()

        #line settings
        self.SerialPortLine.setReadOnly(True)
        self.TemperatureLine.setReadOnly(True)
        self.LogLine.setReadOnly(True)

        #line tool tip
        self.SerialPortLine.setToolTip('Serial port information.')
        self.TemperatureLine.setToolTip('Tank CPU temperature.')
        self.LogLine.setToolTip('Program logs.')

        self.layOutPattern.addWidget(self.SerialPortLine, 1, 0)
        self.layOutPattern.addWidget(self.TemperatureLine, 1, 3)
        self.layOutPattern.addWidget(self.LogLine, 4, 0)
        

    def createLabels(self):
        #lables
        self.SerialPortLabel = QLabel("Serial Port: ", self)
        self.TemperatureLabel = QLabel("Tank CPU temperature: ", self)
        self.LogsLabel = QLabel("Logs: ", self)

        #connect labels to layout
        self.layOutPattern.addWidget(self.SerialPortLabel, 0, 0)
        self.layOutPattern.addWidget(self.TemperatureLabel, 0, 3)
        self.layOutPattern.addWidget(self.LogsLabel, 3, 0)

        self.setLayout(self.layOutPattern)

    def createInterface(self):
        self.layOutPattern = QGridLayout()
        self.createLabels()
        self.createLineEdit()

        #windows settings
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle("Tank GUI")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Gui()
    sys.exit(app.exec_())