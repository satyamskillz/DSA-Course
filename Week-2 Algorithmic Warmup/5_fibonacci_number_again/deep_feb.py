import tensorflow as tf
from tensorflow import keras
import numpy as np
import math

x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]

model=tf.keras.Sequential([
    keras.layers.Dense(units=1,input_shape=[1])
])
model.compile(optimizer="sgd",loss="mean_squared_error")

model.fit(x,y,epochs=5000)

model.save("feb.h5")

value=model.predict([2816213588])
value=math.ceil(value)
print(value,value%239)