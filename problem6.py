squares_sum=0
sum=0

for i in range(1,101):
    squares_sum=squares_sum+(i**2)
    sum=sum+i

print((sum**2)-squares_sum)