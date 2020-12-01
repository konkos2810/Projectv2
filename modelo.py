import parametroi
import encoder
import decoder
import keras
from keras.layers import Input
from keras.models import Model
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt

def modelo(train_X,valid_X,train_ground,valid_ground,data):

	number_of_layers,filter_size,number_of_filters,epochs,batch_size = parametroi.parameters()
	print('//////////////////////////////////////////////////////////////////////////////////////////////')
	inChannel = 1
	x, y = 28, 28
	input_img = Input(shape = (x, y, inChannel))

	conv,enc_layers = encoder.encoder(input_img,filter_size,number_of_filters,number_of_layers) 
	decoded = decoder.decoder(conv,filter_size,number_of_filters,enc_layers,number_of_layers)

	autoencoder = Model(input_img, decoded)
	autoencoder.compile(loss='mean_squared_error', optimizer =	RMSprop())

	model = autoencoder.fit(train_X, train_ground,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_ground))

	return model,epochs,autoencoder