import argparse
from time import time

from keras.models import load_model
import numpy as np
import pandas as pd

# from src.functions import build_model, prep_data, create_dataset


def main(train: str):
    if train == "Train":
        training = True
    elif train == "Eval":
        training = False
    else:
        raise Exception("invalid or missing model instructions (Train or Eval)")

    # load data
    print("\nPENN DATA CHALLENGE\n\n\nLoading Data\n\n")
    data = pd.read_csv("data/bitcoin.csv").drop(
        ["time_period_start", "time_period_end", "time_open", "time_close"], axis=1
    )

    # view data
    print("\nView Data:\n")
    print(data.head())

    # prep data
    print("\n\nPrep Data:")
    clean_data, scaler = prep_data(data)
    trainX, trainY = create_dataset(clean_data, look_back=60)

    # train model
    if training:
        model = build_model()
        start = time()
        history = model.fit(
            trainX, trainY, batch_size=32, epochs=10, validation_split=0.3, verbose=1
        )
        print("\nTraining Time: ", time() - start)
        model.summary()
        # Save Model
        model.save("model/bitcoin_rnn.h5")

    else:
        # load model
        model = load_model("model/bitcoin_rnn.h5")

    # predict
    preds = model.predict(trainX)
    real_pred = scaler.inverse_transform(preds)
    real_price = scaler.inverse_transform(trainY.reshape(-1, 1))

    # evaluate predictions
    rmse = np.sqrt(np.mean(np.square((real_price - real_pred))))
    print("\n\nRMSE: ", rmse)
    print("\nFirst 10 Predictions:\n", real_pred[:10])
    print("\n\nFirst 10 Prices:\n", real_price[:10])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="train new RNN or use previously built model"
    )
    parser.add_argument(
        "--train",
        help="Train or Eval - Train will train new model, Eval will use best previously trained model",
    )
    args = parser.parse_args()
    if args.train not in ["Train", "Eval"]:
        raise Exception("train argument must be Train or Eval")

    main(args.train)
