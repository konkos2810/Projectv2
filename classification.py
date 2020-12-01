import keras
import dataset
import dataset_labels
import parametroi
import modelo
import graphs
import sys
from numpy import array
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import load_model
import numpy as np
from numpy import argmax
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report

argument1 = sys.argv[1]
argument2 = sys.argv[3]
argument3 = sys.argv[5]
argument4 = sys.argv[7]
argument5 = sys.argv[9]

if (argument1=='-d' and argument2=='-dl' and argument3=='-t' and argument4=='-tl' and argument5=='-model'):
	train_file = sys.argv[2]
	trainlabels_file = sys.argv[4]
	test_file = sys.argv[6]
	testlabels_flie = sys.argv[8]
	model_name = sys.argv[10]

print('//////////////////////////////////////////////////////////////////////////////////////////////')
train_data = dataset.dataset(train_file)	#print(train_data[1])
train_data = array(train_data)
print('//////////////////////////////////////////////////////////////////////////////////////////////')
train_labels = dataset_labels.dataset_labels(trainlabels_file)	#print(train_labels[1])
train_labels = array(train_labels)
print('//////////////////////////////////////////////////////////////////////////////////////////////')
test_data = dataset.dataset(test_file)	#print(test_data[1])
test_data = array(test_data)
print('//////////////////////////////////////////////////////////////////////////////////////////////')
test_labels = dataset_labels.dataset_labels(testlabels_flie)	#print(test_labels[1])
test_labels = array(test_labels)
print('//////////////////////////////////////////////////////////////////////////////////////////////')

#change the labels to one-hot encoding
trainlabels_one_hot = to_categorical(train_labels)
testlabels_one_hot = to_categorical(test_labels)

train_X,valid_X,train_label,valid_label = train_test_split(train_data,trainlabels_one_hot,test_size=0.2,random_state=13)

autoencoder = load_model('autoencoder_model.h5')	#model.summary()

def main():
	number_of_layers,filter_size,number_of_filters,epochs,batch_size = parametroi.parameters()
	model,full_model = modelo.modelo(autoencoder,number_of_layers,filter_size,number_of_filters,epochs,batch_size,train_X,train_label,valid_X,valid_label)
	gr = graphs.graph_for_loss(model,epochs)
	graphs_list.append(gr)
	repeat = input('Do you want to make a new model with other parameters?')
	if (repeat == 'yes'):
		main()
	else:
		show_graphs = input('Do you want to show the graphs for every experiment?')
		if (show_graphs == 'yes'):
			for i in range(0,len(graphs_list)):
				print("Graphs for {} experiment".format(i+1))
				graphs_list[i].show()

		makepredictions = input('Do you want to make prediction for the test_data and show some predictions too?')
		if (makepredictions == 'yes'):
			predicted_classes = full_model.predict(test_data)
			predicted_classes = np.argmax(np.round(predicted_classes),axis=1)

			corect = np.where(predicted_classes == test_labels)[0]
			for i,corect in enumerate(corect[0:9]):
				plt.subplot(3,3,i+1)
				plt.imshow(test_data[corect].reshape(28,28), cmap='gray',interpolation='none')
				plt.title('Predicted {}, Class{}'.format(predicted_classes[corect], test_labels[corect]))
				plt.tight_layout()
			plt.show()
			plt.savefig('Graphs/predicted_numbers.png')
		else:
			print('HAVE A NICE DAY!!!')	

graphs_list = []
main()