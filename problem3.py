from math import *
primes=[]
output=[]
#Algorithm for finding prime numbers
def prime_finder(passed):
    prime=True
    number1=passed
    number2=round(sqrt(number1))+1
    for i in range(2,number2):
        if number1%i==0:
            prime=False
            output.append(i)
    return prime

print(prime_finder(600851475143))
for x in output:
    if prime_finder(x)==True:
        primes.append(x)

print(primes)