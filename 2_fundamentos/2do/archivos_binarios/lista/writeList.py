import pickle

data = ['Dragon Ball', 'Ranma 1/2', 'Boku no hero', 'Tate no yuusha', ['Initial D', 'Beck'], 'One Piece']

with open('list.bin','wb') as fh:
        pickle.dump(data,fh)

print('done...')
