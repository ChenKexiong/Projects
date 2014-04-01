# Prime Factorization 
#iterate,while,algorithm
def is_prime(x):
    for i in range(2,int(x ** .5)+1):
        if x % i == 0:
            return False
    return True

def pfact(x):
    pfs = []
    for i in xrange(2,x+1):
        while(x % i == 0):
           if (is_prime(i)):
               pfs.append(i)
               x = x/i
    return pfs

nn = int(raw_input('Input the number to factorize:'))
print pfact(nn)
