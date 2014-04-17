# find closest pair
import math
import random
import numpy

def eulicd(p1,p2):
    return math.sqrt(sum(map(lambda x,y:(x-y) ** 2,p1,p2)))
def oneNorm(p1,p2):
    return sum(map(lambda x,y: abs(x-y),p1,p2))
def infNorm(p1,p2):
    return max(map(lambda x,y: abs(x-y),p1,p2))
def pNorm(p1,p2,p):
    return (sum(map(lambda x,y:(x-y) ** p,p1,p2))) ** (1. /p)
def dist(p1,p2):
    return eulicd(p1,p2)

def bruteForce(mm):
    l = len(mm)
    for i in xrange(l):
        for j in xrange(i+1,l):
            d = dist(mm[i],mm[j])
            if j == 1:
                min = d
                pair = [i,j]
            elif min > d:
                min = d
                pair = [i,j]
    return min,pair

if __name__ == '__main__':
    myMatrix = numpy.random.rand(60,3)
    mindist,minpair = bruteForce(myMatrix)
    print "Found the requrired pair: row %d ,row %d\nThe minimum distance is %f\nThe pair is " % (minpair[0],minpair[1],mindist),myMatrix[minpair[0]],myMatrix[minpair[1]]
