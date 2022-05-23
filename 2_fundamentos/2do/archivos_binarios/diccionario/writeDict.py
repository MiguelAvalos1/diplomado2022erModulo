#
# 2do
#
import pickle

dict={'1989':'Dragon Ball', '1987':'Ranma 1/2', '2016':'Boku no hero', '2019':'Tate no yuusha'}

with open('dictionary.bin','wb') as fh:
    pickle.dump(dict,fh)
print('done...')

