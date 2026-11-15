employee={
    "eid":"101",
    "ename":"Santosh",
    "jobname":"Analyst",
    "sal":45000,
    "loc":"Bangalore"
}
print(employee)
# pop function
v1=employee.pop("jobname")
print(v1)
print(employee)
# popitem function
v2=employee.popitem()
print(v2)
print(employee)
# clear
employee.clear()
print(employee)