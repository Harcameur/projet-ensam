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
    with open(filename, 'r') as file:
        content = file.readlines()
    return content


def serialiser():
    """Convert csv line into python list

    Returns:
        list, list: Tuple of x and y list
    """
    data = get_csv("data.csv")
    x, y = [], []
    for line in data:
        tab_line = line.split(';')
        x.append(float(tab_line[0]))
        y.append(float(tab_line[1]))
    return x, y


def plot_data():
    """Show data graph
    """
    x, y = serialiser()
    plt.plot(x, y)
    plt.show()
