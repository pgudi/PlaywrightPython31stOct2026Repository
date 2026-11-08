'''
Assignment 1: Programmatically add Even numbers in between 20 to 40 and Read Elements in Reverse order.
Step 1: Make sure we can print numbers from 20 to 40
Step 2: Among 20 to 440 print Even numbers
Step 3: Create an empty list
Step 4: Programmatically add Even numbers into empty list
Step 5: Read Elements in Reverse order
'''
evenNumbers=[]

for i in range(20,41):
    if(i % 2 ==0):
        evenNumbers.append(i)

print(evenNumbers)
# Read Reverse order
for i in range(len(evenNumbers)-1, -1,-1):
    print(evenNumbers[i])
