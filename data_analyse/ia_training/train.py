"""TRAIN MODULE: IA Training module
"""

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

from .config import TEST_RATIO

from .numpyfy_data import get_data


def creating_sets(_train_size: int | None) -> tuple:
    """Créer un set de données selon la train_size

    Args:
        _train_size (int | None): taille des jeu de données d'entrainement

    Returns:
        tuple: 4 list cx_train, cx_test, pathologie_train, pathologie_test
    """
    entree, classe = get_data()

    cx_train, cx_test, pathologie_train, pathologie_test =\
        train_test_split(
            entree, classe, train_size=_train_size, test_size=TEST_RATIO)
    return cx_train, cx_test, pathologie_train, pathologie_test


def mlp_apprentissage(
        _cx_train: list, _pathologie_train: list) -> MLPClassifier:
    """Fonction d'apprentissage

    Args:
        _cx_train (list): donnée d'entré d'entrainement
        _pathologie_train (list): donnée de sortie d'entrainement

    Returns:
        MLPClassifier: objet IA
    """
    mlp = MLPClassifier(
        hidden_layer_sizes=(50, 6),
        activation='tanh',
        solver='adam',
        max_iter=1000)

    return mlp
