import sys
import struct as st

def dataset():
	
	argument = sys.argv[1]
	if (argument == '-d'):
		filename = sys.argv[2]
		with open(filename,'rb') as fl:
			fl.seek(0)
			magic_number = st.unpack('>I',fl.read(4))[0]
			print('The magic number of the file is:',magic_number)
			number_of_images = st.unpack('>I',fl.read(4))[0]
			print('The number of images of the file is:',number_of_images)
			number_of_rows = st.unpack('>I',fl.read(4))[0]
			print('The number of rows of the file is:',number_of_rows)
			number_of_columns = st.unpack('>I',fl.read(4))[0]
			print('The number of columns of the file is:',number_of_columns)

			dataset =[]
			for i in range(number_of_images):
				arr=[]
				for i in range(number_of_columns):
					col = []
					for j in range(number_of_rows):
						col.append((st.unpack('B',fl.read(1))[0])/255)
					arr.append(col)
				dataset.append(arr)
	else:
		print('Please give a valid file')

	return dataset