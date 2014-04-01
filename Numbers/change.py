# Change Return Program - The user enters a cost and
# / and %, input
def combination(x):
    money = (.25,.10,.05,.01)
    counts = []
    for i in money:
        a = int(x/i)
        counts.append(a)
        x = x - a*i
    return counts

if __name__ == '__main__':
    cost = input('Input the cost:')
    given = input('Input the money given:')
    change = given - cost
    if change < 0:
        print 'money not enough'
    else:
        (q,d,h,p) = combination(change)
        print 'Should give the customer:\n' + '%d Quaters,%d Dimes,%d Nickels,%d Pennies' % (q,d,h,p)
