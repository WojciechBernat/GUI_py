from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Gui(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.createInterface()
        self.createLabels()
        self.show()

    def createLabels(self):
        #lables
        self.SerialPortLabel = QLabel("Serial Port: ", self)
        self.TemperatureLabel = QLabel("Tank CPU temperature: ", self)
        self.LogsLabel = QLabel("Logs: ", self)

        #connect labels to layout
        self.labelsLayout = QGridLayout()
        self.labelsLayout.addWidget(self.SerialPortLabel, 0, 0)
        self.labelsLayout.addWidget(self.TemperatureLabel, 0, 3)
        self.labelsLayout.addWidget(self.LogsLabel, 3, 0)

        self.setLayout(self.labelsLayout)

    def createInterface(self):


        #windows settings
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle("Tank GUI")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Gui()
    sys.exit(app.exec_())