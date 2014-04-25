# product inventory
class Product:
    '''
    Class  Product
    '''
    def __init__(self, price, pid, qty):
        '''init the object'''
        self.price = price
        self.pid = pid
        self.qty = qty

    def update_qty(self, qty, method='add'):
        if method == 'add':
            self.qty += qty
        elif method == 'substract':
            self.qty = max(0, self.qty - qty)

    def print_product(self):
        print '%d\t%s\t%.02f' % (self.pid, self.qty, self.price)


class Inventory:

    def __init__(self):
        self.products = []

    def add(self, prd):
        self.products.append(prd)

    def print_inventory(self):
        v = 0
        for p in self.products:
            print "%d\t%s\t%.02f\n" % (p.pid, p.qty, p.price)
            v += p.qty * p.price
        print "Total value is: %.02f" % v

if __name__ == '__main__':
    p1 = Product(1.4, 123, 5)
    p2 = Product(1, 334, 100)
    p3 = Product(100.4, 324, 23)

    i = Inventory()
    i.add(p1)
    i.add(p2)
    i.add(p3)

    p1.update_qty(34)
    i.print_inventory()

    p1.update_qty(34, method='substract')
    i.print_inventory()
