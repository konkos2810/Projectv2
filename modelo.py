import keras
import encoder
import fc
from keras.layers import Input
from keras.optimizers import Adam
from keras.models import Model



def modelo(autoencoder,number_of_layers,filter_size,number_of_filters,epochs,batch_size,train_X,train_label,valid_X,valid_label):
	inChannel = 1
	x, y = 28, 28
	input_img = Input(shape = (x, y, inChannel))
	encode,enc_layers = encoder.encoder(input_img,filter_size,number_of_filters,number_of_layers)
	synolika_layers = (2*5) + ((enc_layers-2)*4) + 1

	out = fc.fc(encode)

	full_model = Model(input_img,out)

	for l1,l2 in zip(full_model.layers[:synolika_layers],autoencoder.layers[0:synolika_layers]):
	    l1.set_weights(l2.get_weights())

	for layer in full_model.layers[0:synolika_layers]:
	    layer.trainable = False

	full_model.compile(loss='categorical_crossentropy', optimizer=Adam(),metrics=['accuracy'])

	model = full_model.fit(train_X,train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

	full_model.save_weights('autoencoder_classification.h5')

	for layer in full_model.layers[0:synolika_layers]:
	    layer.trainable = True

	full_model.compile(loss='categorical_crossentropy', optimizer=Adam(),metrics=['accuracy'])

	model = full_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

	full_model.save_weights('classification_complete.h5')

	return model,full_model