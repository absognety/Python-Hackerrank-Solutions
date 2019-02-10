# Enter your code here. Read input from STDIN. Print output to STDOUT
# -*- coding: utf-8 -*-
import math
AB = int(input())
BC = int(input())

if AB == BC:
    print (round(math.degrees(math.asin(1/math.sqrt(2)))),chr(176),sep='')

else:
    x = AB/BC
    print (round(math.degrees(math.atan(x))),chr(176),sep='')
    