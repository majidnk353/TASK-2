#5(sum of digits)
i=int(input("enter positive digits:"))
sum=0
while(i>0):
        sum=sum+i%10
        i=i//10
print(sum)
