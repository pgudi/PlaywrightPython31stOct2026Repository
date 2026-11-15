num=10
def display_numbers():
    global num
    if(num<=20):
        print(num)
        num=num+1
        display_numbers()

display_numbers()
