class Student:
    def __init__(self, name, grade, percent, team):
        self.name = name
        self.grade = grade
        self.percent = percent
        self.team = team

    def studentDetails(self):
        return f"{self.name} is in {self.grade} grade with {self.percent}%, from team {self.team}"
    
team1 = "Team-A"
team2 = "Team-B"

student1 = Student("Anil", "A+", 96, team1)
student2 = Student("Rinku", "A+", 97, team1)
student3 = Student("Shyam", "A+", 98, team1)
student4 = Student("GM", "B", 78, team2)
student5 = Student("Rmm", "C", 65, team2)

print(student1.studentDetails())
print(student2.studentDetails())
print(student3.studentDetails())
print(student4.studentDetails())
print(student5.studentDetails())