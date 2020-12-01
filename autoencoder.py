import dataset
from sklearn.model_selection import train_test_split
import modelo
import graphs

print('//////////////////////////////////////////////////////////////////////////////////////////////')
data = dataset.dataset()	#print(data[1])
print('//////////////////////////////////////////////////////////////////////////////////////////////')
train_X,valid_X,train_ground,valid_ground = train_test_split(data,data,test_size=0.2,random_state=13)

def main():
	model,epochs,autoencoder = modelo.modelo(train_X,valid_X,train_ground,valid_ground,data)
	plt = graphs.graph_for_loss(model,epochs)
	graphs_list.append(plt)
	repeat = input('Do you want to make a new model with other parameters?')
	if (repeat == 'yes'):
		main()
	else:
		show_graphs = input('Do you want to show the graphs for every experiment?')
		if (show_graphs == 'yes'):
			for i in range(0,len(graphs_list)):
				print("Graphs for {} experiment".format(i+1))
				graphs_list[i].show()		

		save_model = input('Do you want to save the model with the latest parameters you give?')
		if (save_model == 'yes'):
			autoencoder.save("autoencoder_model.h5")
			print('model has saved')
			autoencoder.save_weights('autoencoder_weights.h5')
			print('The model weights have saved')
		else:
			print('HAVE A NICE DAY!!!')	

graphs_list = []
main()