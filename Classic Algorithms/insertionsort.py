# insertion sort
def insertionsort(lst):
    l = len(lst)
    for i in range(l-1):
        j = i+1
        while j > 0:
            if lst[j] >= lst[j-1]:
                break
            else:
                lst[j],lst[j-1] = lst[j-1],lst[j]
            j -= 1
    return lst
if __name__ == '__main__':
    myarrary = []
    print 'Input an Integer arrary:\n'
    while 1:
        try:
            n = raw_input('>')
        except:
            print ""
            break
        myarrary.extend([int(i) for i in n.split()])
    print "Original list:",myarrary
    print "Insertion sort result:",insertionsort(myarrary)
