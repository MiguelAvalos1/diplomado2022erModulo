import pickle

tuple=('Dragon Ball', 'Ranma 1/2', 'Boku no hero', 'Tate no yuusha', 'Initial D', 'Beck', 'One Piece')

with open('tuple.bin','wb') as fh:
	pickle.dump(tuple,fh)

print('done...')