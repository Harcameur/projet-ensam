import matplotlib.pyplot as plt
from .setup import CSV_PATH


def get_csv(name):
    filename = CSV_PATH + name
    content = []
    with open(filename, 'r') as file:
        content = file.readlines()
    return content


def serialiser():
    data = get_csv("data.csv")
    X, Y = [], []
    for line in data:
        tab_line = line.split(';')
        X.append(float(tab_line[0]))
        Y.append(float(tab_line[1]))
    return X, Y


def plot_data():
    X, Y = serialiser()
    plt.plot(X, Y)
    plt.show()
