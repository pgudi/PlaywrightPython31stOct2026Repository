# 12. Write a function to Concatenate all Elements of a given String list?
def concate_lists(first, second):
    resultant=[]
    for items in first:
        resultant.append(items)

    for items in second:
        resultant.append(items)

    print(resultant)


x=[10,20,30]
y=[50,60,70,80]
concate_lists(x, y)