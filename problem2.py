total=0
x=1
y=0


while x<4000000 and y<4000000:
    x=x+y
    y=x+y
    if x%2==0 and x<4000000:
        total+=x
    if y%2==0 and x<4000000:
            total+=y

print(total)