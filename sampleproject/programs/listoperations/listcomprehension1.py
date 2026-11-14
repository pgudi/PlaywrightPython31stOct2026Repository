# Without list comprehension
divisiblebynine=[]

for i in range(1,101):
    if(i % 9 ==0):
        divisiblebynine.append(i)

print(divisiblebynine)

print("-----------------------------------")
# With list comprehension
divisiblebynine2=[j for j in range(1,101) if (j % 9 ==0)]
print(divisiblebynine2)