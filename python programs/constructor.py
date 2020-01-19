class Student:
    roll = ""
    gpa = ""


    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa



    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


navin = Student(101,3.0)
#navin.set_value(101,3.0)
navin.display()

rashid = Student(104,2.50)
#rashid.set_value(103,3.10)
rashid.display()


