current=2520
result=0

while True:
    result=0
    for i in range(1,21):
        if (current%i)==0:
            result+=1

    if result==20:
        print(current)
        break
    else:
        current+1

