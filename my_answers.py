import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras

import string, re


# TODO: fill out the function below that transforms the input series
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = series[window_size:]

    for index in range(len(series) - window_size):
        input = series[index : index + window_size]
        X.append(input)

    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:window_size])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    hidden_units = 5
    model = Sequential()
    model.add(LSTM(hidden_units, input_shape=(window_size, 1)))
    model.add(Dense(1))

    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?', ' ']
    
    # Get valid characters
    valid_characters = list(string.ascii_letters)
    valid_characters.extend(punctuation)

    # Get unique characters
    unique_characters = sorted(list(set(text)))

    # Get excluded characters
    exclude_characters = [ch for ch in unique_characters if ch not in valid_characters]

    # Clean the text
    exclude_regex = re.compile('|'.join(map(re.escape, exclude_characters)))
    text = exclude_regex.sub("", text)

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    for index in range(0, len(text) - window_size, step_size):
        input = text[index : index + window_size]
        output = text[index + window_size]
        inputs.append(input)
        outputs.append(output)

    return inputs,outputs

# TODO build the required RNN model:
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss
def build_part2_RNN(window_size, num_chars):
    hidden_units = 200
    model = Sequential()
    model.add(LSTM(hidden_units, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))

    return model
