def parameters():
	number_of_layers = int(input('Please give the number of layers:'))
	print('The number of layers is:',number_of_layers)
	filter_size = int(input('Please give the filter size:'))
	print('The filter size is:',filter_size)
	number_of_filters = []
	for i in range(number_of_layers):
		number = int(input('Please give the number of filters for the {} layer:'.format(i+1)))
		number_of_filters.append(number)
	for i in range(number_of_layers):
		print('The number of filters for the {} layer is:'.format(i+1),number_of_filters[i])
	epochs = int(input('Please give the epochs number:'))
	print('The number of epochs is:',epochs)
	batch_size = int(input('Please give the batch size:'))
	print('The batch size is:',batch_size)	

	return number_of_layers,filter_size,number_of_filters,epochs,batch_size
