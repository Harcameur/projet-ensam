""" Data Module Acquisiton
"""
from .setup import arduino, DATA_LENGTH, CSV_PATH
from .langue import FR


def read_data():
    """Getting arduino data from port

    Returns:
        str: data signal
    """
    line = arduino.readline()
    return line.decode("utf-8")


def get_a_full_dataset():
    """setting up dataset from arduino data

    Returns:
        list: list of data tuple
    """
    i = 0
    dataset = []
    print(FR['DATA_ACQUISITION']['STARTING_MSG'])
    while DATA_LENGTH - i > 0:
        pin = read_data()[:-2]
        if pin != '':
            dataset.append([i, pin])
            i += 1
    print(FR['DATA_ACQUISITION']['FINISH_MSG'])
    print(dataset)
    return dataset


def convert_dataset(dataset):
    """converting python list into csv text

    Args:
        dataset (list): data signal list

    Returns:
        str: csv content
    """
    converted_txt = ""
    for line in dataset:
        converted_txt += str(line[0]) + ';' + str(line[1]) + ';\n'
    return converted_txt


def save_data_csv(name):
    """save data in csv file

    Args:
        name (str): csv filename
    """
    dataset = get_a_full_dataset()
    filename = CSV_PATH + name
    print(filename)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(convert_dataset(dataset))
