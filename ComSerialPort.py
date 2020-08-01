import serial

# Communication with serial port class
class ComSerialPort:

    def __init__(self, serialClass, writeBuffer, readBuffer):
        try:
            if (type(serialClass) != serial.Serial):
                raise TypeError
            else:
                self.__serialPortInstance = serialClass
                print("Correct type of serial port instances.")
        except:
            print("Incorrect type of serial port instances.")

        try:
            if ((ComSerialPort.isList(writeBuffer) or ComSerialPort.isList(readBuffer)) == 1):
                self.__writeBuffer = writeBuffer
                self.__readBuffer = readBuffer
                print("Correct type of read/write buffers.")
            else:
                raise TypeError
        except:
            print("Incorrect type of read/write buffers. Buffers must be list.")

    def readToBuffer(self):
        self.__readBuffer.append(self.__serialPortInstance.readline())

    def writeFromBuffer(self):
        self.__serialPortInstance.write(bytearray(ComSerialPort.lastListElement(self.__writeBuffer), 'utf-8'))
        self.__serialPortInstance.flush()

    @staticmethod
    def isList(array):
        if type(array) == list:
            return 1
        else:
            return -1

    @staticmethod
    def lastListElement(array):
        try:
            if (ComSerialPort.isList(array)):
                return array[-1]
            else:
                raise TypeError
        except:
            print("Incorrect type. It is not a list.")

    @staticmethod
    def hexToString(arg):
        return (str(arg) + '\n')