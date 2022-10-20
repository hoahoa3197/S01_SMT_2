
from socket import timeout
import serial
serialPLC = serial.Serial(port = "COM3", baudrate = 115200,timeout=0.0001)
while True:
    print(serialPLC.readline())