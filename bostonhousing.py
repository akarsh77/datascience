# -*- coding: utf-8 -*-
"""BostonHousing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ALn8394q5fna866zKyiF2pDT2sQwJRHH
"""

import keras
import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')
df=pd.read_csv('drive/My Drive/Colab Notebooks/HousingPrices.csv')
df.head()

X = df.drop(columns=['SalePrice'])
Y = df[['SalePrice']]

model = keras.models.Sequential()

model.add(keras.layers.Dense(8, activation='relu', input_shape=(8,)))
model.add(keras.layers.Dense(8, activation='relu'))
model.add(keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, Y, epochs=30, callbacks=[keras.callbacks.EarlyStopping(patience=3)])

test_data = np.array([2003,	854,	1710,	2,	1,	3,	8,	2008])
print(model.predict(test_data.reshape(1,8), batch_size=1))

model.save('savedmodel.h5')
!ls

old_model = keras.models.load_model('savedmodel.h5')

test_data = np.array([2003,	854,	1710,	2,	1,	3,	8,	2008])
print(old_model.predict(test_data.reshape(1,8), batch_size=1))