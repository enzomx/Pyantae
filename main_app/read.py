import time
import serial


arduino = serial.Serial('COM2', 9600)
time.sleep(2)
rawString = arduino.readline()
arduino.close()