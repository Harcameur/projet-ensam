""" Plotter Module : visualize signal data
"""
import matplotlib.pyplot as plt
from .setup import CSV_PATH


def get_csv(name):
    """read csv file

    Args:
        name (str): csv filename

    Returns:
        content: list  of csv lines
    """
    filename = CSV_PATH + name
    content = []
    with open(filename, 'r', encode="utf-8") as file:
        content = file.readlines()
    return content


def serialiser():
    """Convert csv line into python list

    Returns:
        list, list: Tuple of x and y list
    """
    data = get_csv("data.csv")
    x_data, y_data = [], []
    for line in data:
        tab_line = line.split(';')
        x_data.append(float(tab_line[0]))
        y_data.append(float(tab_line[1]))
    return x_data, y_data


def plot_data():
    """Show data graph
    """
    x_data, y_data = serialiser()
    plt.plot(x_data, y_data)
    plt.show()
