from .setup import arduino;

def read_data():
    line = arduino.readline()
    return line.decode("utf-8") 
