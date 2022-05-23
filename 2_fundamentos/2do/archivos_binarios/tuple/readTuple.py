import pickle
import pprint

with open('tuple.bin','rb') as fh:
        data = pickle.load(fh) 

print(type(data))

pprint.pprint(data)