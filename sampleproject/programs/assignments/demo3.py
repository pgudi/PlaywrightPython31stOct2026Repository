# 3. Write a function based on given input, the key and value pair in dictionary should populate.

def add_data_in_dictionary(dictobject):
    employee={}
    employee.update(dictobject)
    print(employee)


add_data_in_dictionary({"empno":101})
add_data_in_dictionary({"ename":"Santosh"})