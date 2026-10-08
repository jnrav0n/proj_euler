total_found=0
total=0

def odd_checker(numpass):
    if numpass%2==0:
        result=0
    else:
        result=1
    return result

while total_found<=154000:
    num = odd_checker(total_found**2)
    if num==1:
        total+=total_found**2
    total_found+=1

print(total)