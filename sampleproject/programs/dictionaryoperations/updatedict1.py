employee={
    "eid":"101",
    "ename":"Santosh",
    "jobname":"Analyst",
    "sal":45000,
    "loc":"Bangalore"
}
print(employee)
# update the existing dictionary
employee["loc"]="Managalore"
print(employee)
employee.update({"jobname":"Sales Manager"})
print(employee)
employee.update({"country":"India"})
print(employee)