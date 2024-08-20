#7 to find factors of a number
#-----------------------------
while(True):
        n=int(input("enter a number:"))
        i=0
        while(i<n):
                i+=1
                if(n%i==0):
                        print(i)
