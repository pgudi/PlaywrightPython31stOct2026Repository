
def showAllTables():
    for i in range(1,21):
        for k in range(1,11):
            result=f"{i} X {k} = {k * i}"
            print(result)
        print("----------")

showAllTables()
