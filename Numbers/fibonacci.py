# Fibonacci Sequence
# 2 methods
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    fibs = [0]
    while(len(fibs) < n):
        if len(fibs) == 1:
            fibs.append(1)
        else:
            fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == '__main__':
    nn = raw_input('Input a number to cal its fib:')
    #print fib(int(nn))
    print fib2(int(nn))
