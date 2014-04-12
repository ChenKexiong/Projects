# steps from n to 1
def main():
    n = input("Input the starting number:\n")
    steps = 0
    print "%d " % n,
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        steps += 1
        print "->%d " % n,
    print "\nThe total steps are %d" % steps
if __name__ == "__main__":
    main()
