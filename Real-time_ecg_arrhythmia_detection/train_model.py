# C:\Users\laksh\OneDrive\Desktop\ecg_classification\train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout, Reshape, Input
from tensorflow.keras.models import Model

# Load data
ptbdb_normal = pd.read_csv(r'C:\Users\hp\Desktop\ecg_classification\data\ptbdb_normal.csv', header=None)
ptbdb_abnormal = pd.read_csv(r'C:\Users\hp\Desktop\ecg_classification\data\ptbdb_abnormal.csv', header=None)
mitbih_train = pd.read_csv(r'C:\Users\hp\Desktop\ecg_classification\data\mitbih_train.csv', header=None)
mitbih_test = pd.read_csv(r'C:\Users\hp\Desktop\ecg_classification\data\mitbih_test.csv', header=None)

# Ensure each sample has 188 features (truncate or pad if necessary)
def preprocess_data(data):
    processed_data = []
    for sample in data.values:
        if len(sample) > 188:
            processed_data.append(sample[:188])
        elif len(sample) < 188:
            processed_data.append(np.pad(sample, (0, 188 - len(sample)), 'constant'))
        else:
            processed_data.append(sample)
    return np.array(processed_data)

ptbdb_normal = preprocess_data(ptbdb_normal)
ptbdb_abnormal = preprocess_data(ptbdb_abnormal)
mitbih_train = preprocess_data(mitbih_train)
mitbih_test = preprocess_data(mitbih_test)

# Combine PTB data and create labels
ptbdb_data = np.concatenate((ptbdb_normal, ptbdb_abnormal))
ptbdb_labels = np.concatenate((np.zeros(len(ptbdb_normal)), np.ones(len(ptbdb_abnormal))))
ptbdb_labels = to_categorical(ptbdb_labels, 2)

# Split PTB data
ptbdb_train_signals, ptbdb_test_signals, ptbdb_train_labels, ptbdb_test_labels = train_test_split(
    ptbdb_data, ptbdb_labels, test_size=0.2, random_state=42)

# Model creation
def create_model(input_shape):
    signal_input = Input(shape=input_shape)
    x = Reshape((-1, 1))(signal_input)
    x = Bidirectional(LSTM(64, return_sequences=True))(x)
    x = Bidirectional(LSTM(32))(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.5)(x)
    output = Dense(2, activation='softmax')(x)
    model = Model(inputs=signal_input, outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model = create_model((188,))
model.fit(ptbdb_train_signals, ptbdb_train_labels, validation_data=(ptbdb_test_signals, ptbdb_test_labels), epochs=20, batch_size=64)
model.save('C:\\Users\\hp\\Desktop\\ecg_classification\\models\\ecg_classifier_model.h5')