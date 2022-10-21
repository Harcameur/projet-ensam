"""Setup Module: Contain configuration for the project and arduino information
"""
import serial

PORT = 'COM5'
BAUDRATE = 9600
TIMEOUT = .1

arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)

DATA_LENGTH = 2000

CSV_PATH = "data_analyse\\acquisition\\assets\\csv\\"
ACQ_PATH = "data_analyse\\acquisition\\assets\\"

ACQ_LENGHT = 50
