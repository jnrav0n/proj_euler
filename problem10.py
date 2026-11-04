from math import *
primes=[]
total=0

def prime_finder(passed):
    prime=True
    number1=passed
    number2=round(sqrt(number1))+1
    for i in range(2,number2):
        if number1%i==0:
            prime=False
    return prime

for i in range(0,2000000):
    if prime_finder(i)==True:
        primes.append(i)

for x in primes:
    total+=x

print(total)