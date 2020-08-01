
import serial.tools.list_ports

class DetectSerialPort:

    def __init__(self):
        self.__toFind = "Arduino"

    @property
    def toFind(self):
        return self.__toFind

    @toFind.getter
    def toFind(self):
        print("Device to find: " + str(self.__toFind))

    @toFind.setter
    def toFind(self, arg):
        if(type(arg) != str):
            arg = str(arg)
        self.__toFind = arg

    @toFind.deleter
    def toFind(self):
        self.__toFind= ""

    #search list by passed device_Name to find port
    @staticmethod
    def findDeviceInList(deviceName, argList):
        # Begin
        for i in argList:
            for j in i:
                if (j.find(deviceName) != -1):
                    return i
        return -1
        # end

    def findPortInUse(deviceName):
        try:
            if(deviceName == None):
                raise ValueError
            else:
                if(type(deviceName) != str):
                    deviceName = str(deviceName)

                portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
                portList = list(portList)  ##converet to list - each item is list of single serial port

                return DetectSerialPort.findDeviceInList(deviceName,portList)
        except ValueError:
            print("Invalid time out value. \nPass device name has no value!")

    def detectPort(self):
        try:
            portInfo = DetectSerialPort.findPortInUse(self.__toFind)

            if (portInfo == -1):
                raise ValueError
            else:
                print("Detected port: " + str(portInfo[0]))
                return portInfo[0]
        except ValueError:
            print("Port you are looking for was not found.")


