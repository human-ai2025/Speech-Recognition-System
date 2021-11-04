from typing import Tuple, Any
import json
import numpy as np
from sklearn.model_selection import train_test_split
import random
import logging


def init_logger():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.INFO)


def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)


def load_dataset(data_path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    :param data_path: The path of the dataset
    :return:  The X and Y dataset
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    # extract inputs and targets
    X = np.array(data["MFCCs"])
    y = np.array(data["labels"])

    return X, y


def get_dataset(data_path: str) -> Tuple[Any, Any, Any, Any, Any, Any]:
    """
    :param data_path: The path of the dataset
    :return: The list of the splits
    """
    # load the dataset
    print("\n[INFO] The dataset path is ~> ",data_path)
    X, y = load_dataset(data_path)

    # create the train, validation ad test splits
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.1)

    # convert input from 2d to 3d array
    # the ... gets all the dim and new axis add another axis
    x_train = x_train[..., np.newaxis]
    x_val = x_val[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    # return the array
    return x_train, x_val, x_test, y_train, y_val, y_test
