import matplotlib.pyplot as plt

def graph_for_loss(model,epochs):

	epochs = range(1,epochs+1)
	plt.plot(epochs,model.history['loss'],'b')
	plt.plot(epochs,model.history['val_loss'],'r')
	plt.title('Model losses')
	plt.ylabel('Loss')
	plt.xlabel('Epochs')
	plt.legend(['TRAINING LOSS', 'VALIDATION LOSS'])
	plt.savefig('Graphs/graph_for_loss.png')

	return plt