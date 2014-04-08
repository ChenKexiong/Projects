# factorial finder
def fact_loop(n):
    count = 1
    if n > 0:
        for i in range(1,n+1):
            count *= i
    return count

def fact_recur(n):
    if n == 0:
        return 1
    else:
        return fact_recur(n-1) * n

if __name__ == '__main__':
    n = input('Input an integer number(>=0):\n')
    if n >= 0:
        print 'the result using loop is %d' % fact_loop(n)
        print 'the result using recursion is %d' % fact_recur(n)
    else:
        print 'Invalid number'
