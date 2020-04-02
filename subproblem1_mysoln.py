# operations:
# find length (magnitude), sqrt X**2, Y**2, Z**2
# normalize operator: direction
#    divide vector by magnitude
# dot product: [a,b,c] * [d,e,f] = sqrt(ad+be+cf) ?
# v + v, v - v, v*2, v/3

# MY CODE:
import math

def magnitude(arr):
    print(list(map(lambda x: x**2, arr)))

def normalize(arr):
    print(list(map(lambda x: x/x**2, arr)))

def dotproduct(arr1, arr2):
    print(math.sqrt(sum(list(map(lambda x,y:x*y, arr1, arr2)))))

def vectorsum(arr1,arr2):
    print(list(map(lambda x,y: x+y, arr1, arr2)))
    
def vectordiff(arr1, arr2):
    print(list(map(lambda x,y: x-y, arr1, arr2)))

def vectorquot(arr, num):
    print(list(map(lambda x: x/num, arr)))

def vectorprod(arr, num):
    print(list(map(lambda x: x*num, arr)))


# CODE FROM TUTORIAL:

# write tests before implentation?
