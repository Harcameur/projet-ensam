""" Plotter Module : visualize signal data
"""
import matplotlib.pyplot as plt


def get_csv(full_path):
    """read csv file

    Args:
        full_path (str): full path csv filename

    Returns:
        content: list  of csv lines
    """
    content = []
    with open(full_path, 'r', encoding="utf-8") as file:
        content = file.readlines()
    return content


def serialiser(full_path):
    """Convert csv line into python list

    Returns:
        list, list: Tuple of x and y list
    """
    data = get_csv(full_path)
    x_data, y_data = [], []
    for line in data:
        tab_line = line.split(';')
        if len(tab_line) == 3:
            x_data.append(float(tab_line[0]))
            y_data.append(float(tab_line[1]))
    return x_data, y_data


def plot_data(full_path):
    """Show data graph
    """
    x_data, y_data = serialiser(full_path)
    plt.plot(x_data, y_data)
    plt.show()
