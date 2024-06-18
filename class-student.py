# This is the class constructer to store data of students

class student:
    def __init__(self,name,section,age):
        self.name = name
        self.section = section
        self.age = age

    def show_detials(self):
        print(f"Name is {self.name}")
        print(f"Section is {self.section}")
        print(f"Age is {self.age}")

st1 = student("Jatin","A",14)
st2 = student("Joesp","A",13)
st3 = student("Lucky","B",15)

st1.show_detials()
st3.show_detials()
st2.show_detials()