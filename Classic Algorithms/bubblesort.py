# bubble sort
# When input ,press Ctrl + C to stop input
def bubblesort(ls):
    l = len(ls)
    while l > 1:
        for i in range(l-1):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
        l -= 1
    return ls
if __name__ == '__main__':
    lst = []
    print 'Input an Integer arrary:\n'
    while 1:
        try:
            n = raw_input('>')
        except:
            print ""
            break
        lst.extend([int(i) for i in n.split()])
    print "Original list:",lst
    print "Bubble sort result:",bubblesort(lst)
