def division(x,y):
    try:
        result=(x / y)
        print("Division Result :",result)
    except IndexError as e:
        print("Exception :",e)
    finally:
        print("This block execute always!!!")

division(45,9)
division(15,0)