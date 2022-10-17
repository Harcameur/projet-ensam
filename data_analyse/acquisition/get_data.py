from .setup import arduino, DATA_LENGTH
from .langue import FR


def read_data():
    line = arduino.readline()
    return line.decode("utf-8")


def get_a_full_dataset():
    i = 0
    dataset = []
    print(FR['DATA_ACQUISITION']['STARTING_MSG'])
    while DATA_LENGTH - i > 0:
        dataset.append([i, read_data()[:-2]])
        i += 1
    print(FR['DATA_ACQUISITION']['FINISH_MSG'])
    print(dataset)
    return dataset


def save_data_csv():
    dataset = get_a_full_dataset()
