# generate a function to produce points 
# to be used as x-axis
# 
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]


from decimal import Decimal


a=int(input('ingrese punto inicial')) #initial point
b=int(input('ingrese punto final')) #final point
c=Decimal(input('ingrese incremento ')) #increment

i=a
while i<=b:
    # print(i)
    print ("{0:.1f}".format(i))
    i+=c