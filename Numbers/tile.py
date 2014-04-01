# Find Cost of Tile to Cover W x H Floor - Calculate
# useless
cost = input("What's the cost per sq. feet? ")
width = input("What's the width of the floor? ")
height = input("What's the height of the floor? ")

print "The total cost is $%.2f for %.2f square feet" \
      % (width * height * cost, width * height)
