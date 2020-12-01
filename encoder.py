import keras
from keras.layers import Conv2D,MaxPooling2D,BatchNormalization
import math

def encoder(input_img,filter_size,number_of_filters,number_of_layers):

	d = {}
	enc_layers = math.ceil(number_of_layers/2)
	for i in range(1,enc_layers+1):
		if(i == 1):
			eisodos = input_img
		if(i == 2):
			eisodos = d["pool"+str(i-1)]
		if(i == 3):
			eisodos = d["pool"+str(i-1)]
		if(i > 3):
			eisodos = d["conv"+str(i-1)]

		d["conv"+str(i)] = Conv2D(number_of_filters[i-1], (filter_size, filter_size), activation='relu', padding='same')(eisodos)
		d["conv"+str(i)] = BatchNormalization()(d["conv"+str(i)])
		d["conv"+str(i)] = Conv2D(number_of_filters[i-1], (filter_size, filter_size), activation='relu', padding='same')(d["conv"+str(i)])
		d["conv"+str(i)] = BatchNormalization()(d["conv"+str(i)])
		if (i < 3):
			d["pool"+str(i)] = MaxPooling2D(pool_size=(2, 2))(d["conv"+str(i)])

	return d["conv"+str(enc_layers)],enc_layers