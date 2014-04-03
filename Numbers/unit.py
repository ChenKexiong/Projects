# unit converter
# json,dict
from __future__ import division
from urllib2 import urlopen
import json

TO_TABLE = {
        'length':{
            'cm': 0.01,
            'm': 1,
            'km': 1000,
            'mi': 1609.34,
            'ft': 0.3048,
            },
        'temp':{
            'C': 1,
            'F': 33.8,
            }
        }

FROM_TABLE = {
        'length':{
            'cm': 100,
            'm': 1,
            'km': 0.001,
            'mi': 0.000621371,
            'ft': 3.28084,
            },
        'temp':{
            'C': 1,
            'F': -17.2222
            }
        }


def get_inputs(choice):
    units = ', '.join(TO_TABLE[choice].keys())
    funit = raw_input('which is your unit (%s): ' % units)
    fvalue = float(input('input your value:'))
    tunit = raw_input('to which do you convert (%s): ' % units)
    return funit,fvalue,tunit

def get_currency(funit,fvalue,tunit):

    url = 'http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=%s' % (funit,tunit,str(fvalue))
    content = urlopen(url).read()
    return json.loads(content)['v']

def main():
    print """Unit converter:
    1. length
    2. temperature
    3. currency"""
    choice = int(raw_input('Which do you want to choose?'))
    if choice == 1:
        funit,fvalue,tunit = get_inputs('length')
        print '%f%s = %f%s' % (fvalue,funit,fvalue * TO_TABLE['length'][funit] * FROM_TABLE['length'][tunit],tunit)
    elif choice == 2:
        funit,fvalue,tunit = get_inputs('temp')
        if (funit,tunit) == ('F','C'):
            value = (fvalue - 32) * (5/9)
        elif (funit,tunit) == ('C','F'):
            value = (fvalue * (9/5)) + 32
        else:
            value = fvalue
        print '%f%s = %f%s' % (fvalue,funit,value,tunit)
    
    elif choice == 3:
        funit = raw_input('Enter your currency (eg USD,INR etc): ')
        fvalue = float(raw_input('value:'))
        tunit = raw_input('To ?')
        print '%f%s = %f%s' % (fvalue,funit,get_currency(funit,fvalue,tunit),tunit)
    else:
        print 'Invalid choice'

if __name__ == '__main__':
    main()
