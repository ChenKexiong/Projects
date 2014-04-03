# Next Prime Number
# y/n,awsome
def next_prime(n):
    next = n + 1
    i = 2
    while(next > i):#awsome
        if next % i == 0:
            next += 1
            i = 2
        else:
            i += 1
    return next

if __name__ == '__main__':
    nn = 2
    print nn
    while True:
        request = raw_input('Would you like to get the next prime? (y/n)')
        if request.lower().startswith('y'):
            nn = next_prime(nn)
            print nn
        else:
            break
