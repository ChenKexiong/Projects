# coin flip simulation
import random
def flip():
    flip = random.random()
    if flip > .5:
        return True
    else:
        return False
def main(n):
    heads,tails = 0,0
    results = ''
    while n > 0:
        if flip():
            heads += 1
            results += 'H'
        else:
            tails += 1
            results += 'T'
        n -= 1
    return heads,tails,results
if __name__ == '__main__':
    n = input('How many times do you want to try?\n')
    h,t,r = main(n)
    print 'The number of heads is %d\n' % h
    print 'The number of tails is %d\n' % t
    print 'The result is %s\n' % r
