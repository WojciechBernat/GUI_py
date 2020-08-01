import time
import serial
from DetectSerialPort import DetectSerialPort
from SpecialSerialPort import SpecialSerialPort


arduinoSerialPort = serial.Serial('COM3', 115200, timeout=0.2, write_timeout=0.2)

test_object = SpecialSerialPort(arduinoSerialPort)

test_object.commandDictionary

test_object.executeCommand("BeginCmd")
test_object.executeCommand("EndCmd")
test_object.executeCommand("TelemetryCmd")

#
# for i in range(4):
#     test_object.comLayer.readToBuffer()
#
# test_object.readingBuffer
# test_object.writtingBuffer


arduinoSerialPort.close()





