# happy numbers

def is_happy_number(n):
    if n == 1:
        return True
    a = str(n)
    b = 0
    for i in a:
        b += int(i) ** 2
    if b in c:
        return False
    else:
        c.append(b)
        return is_happy_number(b)

if __name__ == '__main__':
    n = input('Start at:\n')
    j = 8
    happy_numbers = []
    while j>0:
        c = []
        if is_happy_number(n):
            happy_numbers.append(n)
            j -= 1
        n += 1
    print happy_numbers
