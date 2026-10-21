from math import *
primes=[]
total=0
for i in range(2,2000001):
    prime=True
    number1=i
    number2=round(sqrt(number1))+1
    for x in range(2,number2):
            if number1%x==0:
                prime=False
            else:
                total+=x

