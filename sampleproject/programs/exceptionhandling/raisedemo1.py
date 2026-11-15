#Verify the given number is positive
def verify_positive_number(num):
    try:
        if(num<0):
            raise Exception("The given input is a negative number, provide valid positive number")
        else:
            print(num," is a Positive Number")
    except Exception as e:
        print("Exception :",e)

verify_positive_number(45)
verify_positive_number(-22)