"""NUMPYFY DATA MODULE : Convert csv data into numpy file
(Speed up training)
"""

import numpy as np
import pandas as pd

from .config import SAVE_DATA_PATH, TEST_ASSETS_PATH


def get_test_assets() -> pd:
    """Get all CSV data file tests_assets File come from Kabble

    Returns:
        pd: Panda Object: Concatenate frames
    """
    df0 = pd.read_csv(
        TEST_ASSETS_PATH + "0.csv", header=None)
    df1 = pd.read_csv(
        TEST_ASSETS_PATH + "1.csv", header=None)
    df2 = pd.read_csv(
        TEST_ASSETS_PATH + "2.csv", header=None)
    df3 = pd.read_csv(
        TEST_ASSETS_PATH + "3.csv", header=None)
    return pd.concat([df0, df1, df2, df3], axis=0)


def convert_panda_to_numpy() -> np.array:
    """Convert Panda into Numpy table

    Returns:
        np.array: all data from files
    """
    npfy = get_test_assets().to_numpy()
    # print(npfy.shape)
    return npfy


def save_np_data():
    """Save into NPZ file data to speed up future loading
    """
    np.save(SAVE_DATA_PATH, convert_panda_to_numpy())


def get_data() -> tuple:
    """Return data from NPZ File

    Returns:
        tuple: data entre, classe from npz file into numpy table
    """
    file = np.load(SAVE_DATA_PATH+".npy")
    entree, classe = file[:, :63], file[:, 64]
    return entree, classe


if __name__ == "__main__":
    save_np_data()
