flag=0
num=int(input("Enter The Number to Verify for Prime Number : \n"))
for i in range(2,num):
    if(num % i ==0):
        flag=flag+1
        break

if(flag==0):
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")
