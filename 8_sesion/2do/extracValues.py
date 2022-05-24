import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')


print('head',iris.head())
print('')

print('-------------------------TUPlA-------------------------')
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal length'])
data = []
for i in iris.index:
    data.append(tuple(iris.values[i]))
allnodes = tuple(data)
print(allnodes)



print('------------------------- Dictionario-------------------------')
dict_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal width']).to_dict()
print(dict_from_csv)



print('-------------------------Lista-------------------------')
list_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',names = ['sl','sw','pl','pw','class'])
list = list_from_csv.pl.to_list()
print(list)