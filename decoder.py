import keras
from keras.layers import Conv2D,UpSampling2D,BatchNormalization

def decoder(conv,filter_size,number_of_filters,enc_layers,number_of_layers):

	d = {}
	for i in range(enc_layers+1,number_of_layers+1):
		if(i == enc_layers+1):
			eisodos = conv
		if(i == number_of_layers):
			eisodos = d["up"+str(1)]
		if(i > (enc_layers+1) and i <= (number_of_layers-1)):
			eisodos = d["conv"+str(i-1)]

		d["conv"+str(i)] = Conv2D(number_of_filters[i-1], (filter_size, filter_size), activation='relu', padding='same')(eisodos)
		d["conv"+str(i)] = BatchNormalization()(d["conv"+str(i)])
		d["conv"+str(i)] = Conv2D(number_of_filters[i-1], (filter_size, filter_size), activation='relu', padding='same')(d["conv"+str(i)])
		d["conv"+str(i)] = BatchNormalization()(d["conv"+str(i)])
		if(i == (number_of_layers-1)):
			d["up"+str(1)] = UpSampling2D((2,2))(d["conv"+str(i)])
		if(i == number_of_layers):
			d["up"+str(2)] = UpSampling2D((2,2))(d["conv"+str(i)])
			decoded = Conv2D(1, (filter_size, filter_size), activation='sigmoid', padding='same')(d["up"+str(2)])

	return decoded