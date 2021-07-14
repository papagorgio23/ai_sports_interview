from time import time

import numpy as np
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam


def prep_data(dataset):
    dataset = dataset["price_high"].values.astype("float32")
    dataset = dataset.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    return dataset, scaler


def create_dataset(dataset, look_back=60):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i : (i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    dataX = np.array(dataX)
    dataY = np.array(dataY)
    dataX = np.reshape(dataX, (dataX.shape[0], 1, dataX.shape[1]))

    return dataX, dataY


def build_model(node_1=100, node_2=100, dropout_1=0.2, dropout_2=0.2):
    # initialize model
    model = Sequential()

    # first RNN LSTM layer
    model.add(LSTM(node_1, return_sequences=True))
    model.add(Dropout(dropout_1))

    # second RNN LSTM layer
    model.add(LSTM(node_2, return_sequences=False))
    model.add(Dropout(dropout_2))

    # Output layer
    model.add(Dense(1))
    model.add(Activation("linear"))

    start = time()
    model.compile(loss="mse", optimizer=Adam(learning_rate=0.01))
    print("compilation time : ", time() - start)

    return model
