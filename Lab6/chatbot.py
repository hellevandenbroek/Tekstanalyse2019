from keras.models import Sequential


from keras.models import Sequential
from keras.layers import Dense, Activation
model = Sequential()
# the first layer
model.add(Dense(32, input_dim=16))
# after the first layer, you don't need to specify
# the size of the input anymore:
model.add(Dense(8))

from keras.layers import Input, Dense
from keras.models import Model
inputs = Input(shape=(784,))
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
outputs = Dense(10, activation='softmax')(x)
model = Model(inputs=inputs, outputs= outputs)
model.compile(optimizer='rmsprop’, loss='categorical_crossentropy’,
metrics=['accuracy'])
model.fit(data, labels)

from keras import losses
model.compile(loss=losses.mean_squared_error,
optimizer='sgd’)
# or you can pass the loss name
model.compile(loss='mean_squared_error',
optimizer='sgd')

model.fit(x_train,y_train, epochs=10, batch_size=32)

model.evaluate(x, y, batch_size=32,verbose=1,
sample_weight, steps)
