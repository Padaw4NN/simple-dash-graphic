#!/bin/python3.9
# Author: Alexander Cardoso

import random 
import warnings
warnings.simplefilter("ignore")

import numpy as np 
import pandas as pd 


def setRandIndex(sizeof_data: int, size: float=None) -> np.array:
    indexes: list = []
    size__:  int  = int(sizeof_data * size)
    for idx in range(size__):
        rand = random.randint(0, sizeof_data)
        if rand not in indexes:
            indexes.append(rand)
        else:
            continue
    if len(indexes) == (len(indexes) - 1):
        indexes.append(rand)
    return np.asarray(indexes)

def filter(dataframe: pd.DataFrame, filter_column: str, classes: list) -> pd.DataFrame:
    datas:   list = []
    not_rep: list = []
    for class__ in classes:
        perc_val: float = random.randint(0, 5) * 0.1
        if perc_val >= 0.1 and perc_val not in not_rep:
            not_rep.append(perc_val)
            filter__ = dataframe[dataframe[filter_column] == class__]
            indexes  = setRandIndex(filter__.shape[0], perc_val)
            filter__ = filter__.drop(indexes)
        datas.append(filter__)
    return pd.concat(datas)

def filter(dataframe: pd.DataFrame, drop_size: float=None) -> pd.DataFrame:
    global size
    if not drop_size:
        size = random.randint(0, 5) * 0.1
    else:
        size = drop_size
    indexes = setRandIndex(dataframe.shape[0] - 20, size=size)
    dataframe = dataframe.drop(index=indexes)
    return dataframe


def run(data: str, drop_size: float=None) -> pd.DataFrame:
    df = pd.read_csv(data)
    return filter(df, drop_size)