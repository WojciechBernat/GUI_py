import time
import serial
from ComSerialPort import ComSerialPort
from DetectSerialPort import DetectSerialPort

class SpecialSerialPort:
    #constructor - init pyserial class
    # default:
    # port: None
    # baudrate = 115200
    # the rest by default

    __commandList ={0xAAA: "BeginCmd",
                    0xAAB: "EndCmd",
                    0xAAC: "TelemetryCmd"}
    __rwTimeOut = 1.5

    def __init__(self, serialClass = serial.Serial(None, 115200) ):
        try:
            if (type(serialClass) != serial.Serial):
                raise TypeError
            else:
                self.__serialPortInstance = serialClass  # serial port class from PySerial
                print("Correct type of serial port instances.")
        except:
            print("Incorrect type of serial port instances.")
        self.__writeBuffer = []
        self.__readingBuffer = []
        self.__mainDataBuffer = []
        self.comLayer = ComSerialPort(self.__serialPortInstance, self.__writeBuffer, self.__readingBuffer)
        self.comDetect = DetectSerialPort()
        # print(self.comLayer)
        # print(self.comDetect)

    #main data buffer in place where date will be copy after receive
    #in this array you can add your specify buffer.
    # i.e. __mainDataBuffer = [temperature, voltage, speed, preasure]

    # print logs function
    def initLog(self):
        print("Passed serial port object: " + str(self.__serialPortInstance))

    #reading buffer
    @property
    def readingBuffer(self):
        return self.__readingBuffer

    @readingBuffer.getter
    def readingBuffer(self):
        print("Reading Buffer content: " + str(self.__readingBuffer))

    @readingBuffer.setter
    def readingBuffer(self, data):
        self.__readingBuffer.append(data)

    @readingBuffer.deleter
    def readingBuffer(self):
        self.__readingBuffer.clear()

    #writing buffer
    @property
    def writtingBuffer(self):
        return self.__writeBuffer

    @writtingBuffer.getter
    def writtingBuffer(self):
        print("Writting Buffer content: " + str(self.__writeBuffer))

    @writtingBuffer.setter
    def writtingBuffer(self, data):
        self.__writeBuffer.append(data)

    @writtingBuffer.deleter
    def writtingBuffer(self):
        self.__writeBuffer.clear()

    ##main data buffer
    @property
    def mainDataBuffer(self):
        return self.__mainDataBuffer

    @mainDataBuffer.getter
    def mainDataBuffer(self):
        print("Main data buffer content: " + str(self.__mainDataBuffer))

    @mainDataBuffer.setter
    def mainDataBuffer(self, arg):
        return self.__mainDataBuffer.append(arg)

    @mainDataBuffer.deleter
    def mainDataBuffer(self):
        return self.__mainDataBuffer.clear()

    #command's dictionary
    @property
    def commandDictionary(self):
        print(self.__commandList)

    @commandDictionary.getter
    def commandDictionary(self):
        for i, j in self.__commandList.items():
            print("Hex code: {0}, Name: {1}".format(hex(i), j))

    @commandDictionary.setter
    def commandDictionary(self, newCmdName):
        if type(newCmdName) != str:
            newCmdName = str(newCmdName)
        __newCmdKey = list(self.__commandList.keys())[-1]
        __newCmdKey += 1
        self.__commandList[__newCmdKey] = newCmdName

    def getCommandKey(self, cmdName):
        if type(cmdName) != str:
            cmdName = str(cmdName)

        notFoundCounter = 0;
        dictLen = len(self.__commandList)
        for key,val in self.__commandList.items():
            if val == cmdName:
                return  key

            notFoundCounter += 1
            if notFoundCounter == (dictLen):
                print("Command not found.")
                return -1

    def removeCommand(self, cmdName):
        if type(cmdName) != str:
            cmdName = str(cmdName)

        notFoundCounter = 0;
        dictLen = len(self.__commandList)
        for key,val in self.__commandList.items():
            if val == cmdName:
                print("Found command to remove. \nKey: {0}, Name: {1}".format( str(key), str(val)))
                self.__commandList.pop(key)
                break #break loop executing - found command to remove

            notFoundCounter += 1
            if notFoundCounter == (dictLen):
                print("Command to remove not found.")
                break  # break loop - command not found

    #Read/Write time out
    @property
    def readWriteTimeOut(self):
        return self.__rwTimeOut

    @readWriteTimeOut.getter
    def readWriteTimeOut(self):
        #print("Read/Write time out: " + str(self.__rwTimeOut))
        return self.__rwTimeOut

    @readWriteTimeOut.setter
    def readWriteTimeOut(self, timeout):
        try:
            if (timeout < 0):
                raise ValueError
            else:
                self.__rwTimeOut = timeout
        except ValueError:
            print("Invalid time out value. \nValue less than 0!")

    #execute commands
    def executeCommand(self, cmd):
        key = self.getCommandKey(cmd)
        try:
            if( key < 1):
                raise ValueError
            else:
                self.writtingBuffer = (str(key) + '\n')
                print("Command correct. Append to write buffer.")

                if (self.__rwTimeOut < 0):
                    self.__rwTimeOut = 1
                    print("Read-Write timeout less than 0. Set rwTimeOut = 1")

                # prepare serial port's hardware buffer
                self.__serialPortInstance.reset_input_buffer()
                self.__serialPortInstance.reset_output_buffer()

                self.comLayer.writeFromBuffer()
                time.sleep(self.__rwTimeOut)
                self.comLayer.readToBuffer()

                # logs
                print("Reading buffer: ", self.__readingBuffer)
                print("Write buffer: ", self.__writeBuffer)
        except:
            print("Command value error. Incorrect command.")



