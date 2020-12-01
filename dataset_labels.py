import sys
import struct as st

def dataset_labels(filename):
	
	with open(filename,'rb') as fl:
		fl.seek(0)
		magic_number = st.unpack('>I',fl.read(4))[0]
		print('The magic number of the file is:',magic_number)
		number_of_items = st.unpack('>I',fl.read(4))[0]
		print('The number of items of the file is:',number_of_items)

		dataset =[]
		for i in range(number_of_items):
			dataset.append((st.unpack('B',fl.read(1))[0]))

	return dataset