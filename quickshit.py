# operations:
# find length (magnitude), sqrt X**2, Y**2, Z**2
# normalize operator: direction
#    divide vector by magnitude
# dot product: [a,b,c] * [d,e,f] = sqrt(ad+be+cf) ?
# v + v, v - v, v*2, v/3

def magnitude(arr):
    print(list(map(lambda x: x**2, arr)))

def normalize(arr):
    print(list(map(lambda x: x/x**2, arr)))

normalize([1,2,3])
