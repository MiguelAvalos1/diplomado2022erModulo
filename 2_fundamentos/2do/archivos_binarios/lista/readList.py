import pickle

with open('list.bin','rb') as fh:
        data = pickle.load(fh) 

print(type(data))
print(data)
