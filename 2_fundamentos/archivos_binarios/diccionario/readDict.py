#
# read binary file (dictionary)
# and print it
#

import pickle
import pprint


with open('dictionary.bin','rb') as fh:
	data = pickle.load(fh) 

print(type(data))
pprint.pprint(data)
