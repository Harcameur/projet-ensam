"""TRAIN MODULE: IA Training module
"""

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from joblib import dump

from .config import ACTIVATION, CEL_LAYER, IA_SAVING_PATH, MAX_ITER, SOLVER,\
    TEST_RATIO
from .langue import LANG
from .numpyfy_data import get_data


def creating_sets(_train_size: int | None = None) -> tuple:
    """Créer un set de données selon la train_size

    Args:
        _train_size (int | None): taille des jeu de données d'entrainement

    Returns:
        tuple: 4 list _e_train, _e_test, _classe_train, _classe_test
    """
    entree, classe = get_data()

    _e_train, _e_test, _classe_train, _classe_test =\
        train_test_split(
            entree, classe, train_size=_train_size, test_size=TEST_RATIO)
    print(LANG.get('SHAPE_SUMMARY')(
        _e_train.shape, _e_test.shape, _classe_train.shape,
        _classe_test.shape))
    return np.array(_e_train),\
        np.array(_e_test),\
        np.array(_classe_train),\
        np.array(_classe_test)


def mlp_learning(
        _e_train: list, _classe_train: list) -> MLPClassifier:
    """Fonction d'apprentissage

    Args:
        _e_train (list): donnée d'entré d'entrainement
        _classe_train (list): donnée de sortie d'entrainement

    Returns:
        MLPClassifier: objet IA
    """
    mlp = MLPClassifier(
        hidden_layer_sizes=CEL_LAYER,
        activation=ACTIVATION,
        solver=SOLVER,
        max_iter=MAX_ITER)
    mlp.fit(
        np.array(_e_train),
        np.array(_classe_train))  # apprentissage
    return mlp


def train_with_sets():
    """Training + Saving (optionnal) IA model printing score
    """
    _e_train, _e_test, _classe_train, _classe_test = creating_sets()
    _mlp = mlp_learning(_e_train, _classe_train)
    _score_test, _score_train = _mlp.score(_e_test, _classe_test),\
        _mlp.score(_e_train, _classe_train)
    print(LANG.get('SCORE_TRAIN')(_score_train))
    print(LANG.get('SCORE_TEST')(_score_test))
    _save_bool = input(LANG.get("SAVING_ASK"))

    if _save_bool == "y":
        _save_name = input(LANG.get('SAVENAME_ASK'))
        if _save_name != " " or _save_name != "":
            save_mlp(_mlp, _save_name)
        else:
            save_mlp(_mlp)
    else:
        _retry_bool = input(LANG.get("RETRY_ASK"))
        if _retry_bool == "y":
            train_with_sets()


def save_mlp(_mlp: MLPClassifier, _save_name: str = "autosave") -> None:
    """Save object Classifier into jobfile to be reused

    Args:
        _mlp (MLPClassifier): ia object which would be saved
        _save_name (str, optional): Save filename. Defaults to "autosave".
    """
    print(LANG.get('SAVING_START'))
    dump(_mlp, IA_SAVING_PATH + _save_name + '.joblib')
    print(LANG.get('SAVING_COMPLETED'))
