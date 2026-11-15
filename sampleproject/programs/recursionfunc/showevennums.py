num=20

def show_even_numbers():
    global num
    if(num<=40):
        if(num % 2 ==0):
            print(num)
        num=num+1
        show_even_numbers()


show_even_numbers()