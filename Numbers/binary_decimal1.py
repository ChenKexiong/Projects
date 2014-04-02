# binary to decimal, decimal to binary
def b2d(b):
    bb = str(b)
    bb = bb[::-1]
    count,order = 0,0
    for i in bb:
        count += int(i) * (2 ** order)
        order += 1
    return count

def d2b(d):
    ls = []
    while d != 0:
        ls.append(str(d % 2))
        d /= 2
    ls.reverse()
    b = "".join(ls)
    return int(b)

if __name__ == '__main__':
    print """
    1. binary to decimal
    2. decimal to binary\n
    """
    choice = int(raw_input("choose 1 or 2:"))
    if choice == 1:
        binary = input("input a binary:")
        print "binary to decimal of %d is %d" % (binary,b2d(binary))
    elif choice == 2:
        decimal = input("input a decimal:")
        print "decimal to binary of %d is %d" % (decimal,d2b(decimal))
    else:
        print "Invalid choice"

