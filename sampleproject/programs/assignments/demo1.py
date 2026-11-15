# 1. Write a function for a given tuple, assign all tuple elements into list and Read Elements from list.

def assign_to_list(tupleobject):
    listflowers=[]
    # Assign
    for i in range(0, len(tupleobject)):
        listflowers.append(tupleobject[i])
    #Read
    for item in listflowers:
        print(item, end="  ")


flowers=("Lotus","Lilly","sunflower","Rose","cosmos","Lavendar")
assign_to_list(flowers)