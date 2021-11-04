# import libraries
import tensorflow.keras as tf
from typing import Tuple, Any


def build_model(input_shape: Tuple[Any, Any, Any], OUTPUT: int = 10, error: str = "sparse_categorical_crossentropy",
                LR: float = 0.001) -> tf.Sequential:
    # build the model
    model = tf.Sequential()

    # conv layer 1
    model.add(tf.layers.Conv2D(64, (3, 3), activation="relu",
                               input_shape=input_shape))
    model.add(tf.layers.BatchNormalization())
    model.add(tf.layers.MaxPool2D((3, 3), strides=(2, 2), padding="same"))

    # conv layer 2
    model.add(tf.layers.Conv2D(32, (3, 3), activation="relu"))
    model.add(tf.layers.BatchNormalization())
    model.add(tf.layers.MaxPool2D((3, 3), strides=(2, 2), padding="same"))

    # conv layer 3
    model.add(tf.layers.Conv2D(32, (2, 2), activation="relu"))
    model.add(tf.layers.BatchNormalization())
    model.add(tf.layers.MaxPool2D((2, 2), strides=(2, 2), padding="same"))

    # flatten and feed it to the dense layer
    model.add(tf.layers.Flatten())
    model.add(tf.layers.Dense(128, activation="relu"))
    model.add(tf.layers.Dropout(0.4))

    # softmax classifier
    model.add(tf.layers.Dense(OUTPUT, activation="softmax"))

    # compile the model
    optimiser = tf.optimizers.Adam(learning_rate=LR)
    model.compile(optimizer=optimiser, loss=error, metrics=["accuracy"])

    # print the overall model
    model.summary()

    # return
    return model
