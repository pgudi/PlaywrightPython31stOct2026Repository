num=1
def show_divisible_by_nine():
    global num
    if(num<=100):
        if(num % 9 ==0):
            print(num)
        num=num+1
        show_divisible_by_nine()

show_divisible_by_nine()