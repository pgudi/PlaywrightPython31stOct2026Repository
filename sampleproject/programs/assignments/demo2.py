# 2. Write a function for given dictionary, assign all values into a list and read elements from list.
def assign_vlaues_to_list(dictobject):
    listemployee=[]
    #assign
    for value in employee.values():
        listemployee.append(value)
    #Read Elements from list
    for item in listemployee:
        print(item,"  ")

employee={"empid":101,"ename":"Santosh","job":"Analyst","sal":35000,"dname":"Research"}
assign_vlaues_to_list(employee)

