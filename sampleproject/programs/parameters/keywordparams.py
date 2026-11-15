
def show_student_details(**kwargs):
    for k,v in kwargs.items():
        print(k, " ->", v)
    print("----------")

show_student_details(rollno=101,firstname="Santosh",course="Medical")
show_student_details(firstname="Srinivasa",course="Computer Science")
show_student_details(rollno=101,firstname="Sahana",cityname="Boston",course="Mathemtics")