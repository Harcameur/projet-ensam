import serial;

PORT = 'COM5'
BAUDRATE = 9600
TIMEOUT= .1

arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)

DATA_LENGTH = 1000