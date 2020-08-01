import time

import serial
import serial.tools.list_ports

arduinoSerialReadingBuffer = []
arduinoBeginCmd = '0XAAA\n'
arduinoEndCmd = '0XAAC\n'
arduinoTelemetryCmd = '0XAAC\n'  ##HEX:AAA

byteToRead = 0
readWriteTimeOut = 1.5
deadTimeOut = 1

temperatureBuffer = []
voltageBuffer_1 = []
voltageBuffer_2 = []
batteryBuffer = []
telemetryBuffer = [temperatureBuffer, voltageBuffer_1, voltageBuffer_2, batteryBuffer]


def executeCommand(serialPortInstance, cmd, readBuffer, readWriteTimeOut):
    # validate arguments
    if (readWriteTimeOut < 0):
        readWriteTimeOut = 0

    # Begin
    print("Execute command:", cmd)

    serialPortInstance.reset_output_buffer()
    serialPortInstance.reset_input_buffer()
    clearBuffer(readBuffer)  # preclear buffer

    serialPortInstance.write(bytearray(cmd, 'utf-8'))  ##Send command to slave
    serialPortInstance.flush()
    time.sleep(readWriteTimeOut)  # Dead time between write command and read slave's response

    # readBuffer.append(serialClass.read_until('\n', 32))

    if cmd == arduinoTelemetryCmd:
        for x in range(4):
            readBuffer.append(serialPortInstance.readline())
    else:
        readBuffer.append(serialPortInstance.readline())

    if readBuffer:
        print("Read buffer: ", readBuffer)

    serialPortInstance.reset_output_buffer()
    serialPortInstance.reset_input_buffer()
    # End


def readToBuffer(buffer, serialPortInstance):
    # Begin
    if isinstance(buffer, list):
        buffer.append(serialPortInstance.read_until('\n', 32))
    else:
        buffer = serialPortInstance.readline()
    # End


def clearBuffer(buffer):
    # Begin
    if isinstance(buffer, list):
        buffer.clear()
    elif isinstance(buffer, str):
        buffer = '0'
    elif isinstance(buffer, int):
        buffer = 0
    else:
        print("Unsupported type. Cannot clean buffer.")
    # End


def pickOutSerialPort(deviceName, logFlag=1):
    # Begin
    portInfo = findArduino(deviceName, logFlag)

    if portInfo != -1:
        if logFlag:
            print(portInfo)
            print(portInfo[0])
        return portInfo[0]
    else:
        return -1
    # End


def findArduino(deviceName, logFlag=0):
    # Begin
    if logFlag:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(deviceName, portList)  #############3

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
            else:
                print("Found port:", arduinoPort)  # print log
                return arduinoPort
        except ValueError:
            print("ValueError: no sought serial port detected.")

    else:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(deviceName, portList)  #############

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
            else:
                return arduinoPort
        except ValueError:
            print("ValueError: no serial port detected.")

    # End


def findArduinoPort(deviceName, argList):
    # Begin
    for i in argList:

        for j in i:
            if (j.find(deviceName) != -1):
                return i

    return -1
    # end


def calcAverage(sourceList):
    if (sourceList == None):
        return -1;
    length = len(sourceList)
    if (length <= 0):
        return -1
    else:
        sumList = sum(sourceList)
        avgTemp = sumList / (length)
        return avgTemp;


def decodeStringToFloat(sourceList):
    if (sourceList == None):
        return -1;
    else:
        destinyList = [float(i) for i in sourceList]
        #    print("Destiny list: ", destinyList)
        return destinyList


    # if (type(sourceList) == list):
    #     for i in sourceList:
    #         destinyList = float(i)
    #     #    print("Destiny list: ", destinyList)
    #     return destinyList;
    # else:
    #     destinyList = float(sourceList)
    # #    print("Destiny list: ", destinyList)
    #     return destinyList;


##Init
arduinoSerialPort = serial.Serial(pickOutSerialPort("Arduino Uno"), 115200, timeout=0.2, write_timeout=0.2)

executeCommand(arduinoSerialPort, arduinoBeginCmd, arduinoSerialReadingBuffer, readWriteTimeOut)

for i in range(3):
    executeCommand(arduinoSerialPort, arduinoTelemetryCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
    for j in range(len(telemetryBuffer)):
        telemetryBuffer[j].append(arduinoSerialReadingBuffer[j])

# print(telemetryBuffer)
executeCommand(arduinoSerialPort, arduinoEndCmd, arduinoSerialReadingBuffer, readWriteTimeOut)


for j in range(len(telemetryBuffer)):
    print(calcAverage(decodeStringToFloat(telemetryBuffer[j])))

arduinoSerialPort.close()
