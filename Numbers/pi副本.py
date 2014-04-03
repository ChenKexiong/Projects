## Find PI to the Nth Digit
# print,Machin-like formula
import math
ndigits = raw_input('Input the number of decimals of PI you want to get:')
#using Machin-like formula
print ('{0:.%df}' % min(20,int(ndigits))).format(4 * (4 * math.atan(1.0/5) -math.atan(1.0/239 )))
