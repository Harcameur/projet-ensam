"""Setup Module: Contain configuration for the project and arduino information
"""
import serial

from .error import error_message


PORT = 'COM5'
BAUDRATE = 9600
TIMEOUT = .1

DATA_LENGTH = 1000

CSV_PATH = "data_analyse\\acquisition\\assets\\csv\\"
ACQ_PATH = "data_analyse\\acquisition\\assets\\data\\"

ACQ_LENGHT = 5

IDS_SOLUTION = ['0', '1', '2']


def arduino_setup():
    try:
        return serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    except Exception as e:  # pylint: disable=W0703
        error_message('Arduino Exception', e)


arduino = arduino_setup()
