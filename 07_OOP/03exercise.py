class Student:
    def __init__(self, name, rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def displayInfo(self):
        print("Name:", self.name)
        print("Roll No:", self.rollNo)
        print("Marks:", self.marks)
        
    

student1 = Student("Anil Yadav", "22UCH045", "7.32")

student1.displayInfo()