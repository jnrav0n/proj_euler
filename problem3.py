current=2520
while True:
    result=0
    for i in range(1,21):
        if (current%i)==0:
            result+=1
        else:
            break

    if result==20:
        print(current)
        break
    else:
        current=current+2520
