from random import *

digits=[0,1,2,3,4,5,6,7,8,9]
pos=[]


for i in range(9*8*7*6*5*4*3*2*10):
    for x in range(1,10):
        num1=randint(1,len(digits)-1)
        digit1=digits[num1]
        digits.pop(num1)
        pos.append(digit1)

print(pos)