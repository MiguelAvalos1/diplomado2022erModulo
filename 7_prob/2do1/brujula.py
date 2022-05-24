import numpy 

brujula = [ 'norte', 'sur', 'este', 'oeste' ]

def selectRandom ( brujula ) :
  return numpy.random.choice ( brujula, 4 )

print( "Direcciones cardinales: ", selectRandom( brujula ) )