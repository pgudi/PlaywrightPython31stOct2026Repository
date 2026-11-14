# Without List Comprehension
list=[]
for i in range(20, 31):
    list.append(i)

print(list)

print("--------------------")
# With List Comprehension
numbers=[j for j in range(20,31)]
print(numbers)