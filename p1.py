print("Prime number in range of 200 : ")
for i in range(1,200):
    count=0
    flag=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        if count>2:
            flag=1
            break
    if i!=1 and  flag==0:
        print(i)