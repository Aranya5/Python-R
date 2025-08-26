def averagem(a,b,c):
    return (a+b+c)/3
class Student:
    college_name="HITK"
    student_count=0
    def __init__(self, s, n, m1, m2, m3):
        self.stdid = s
        self.name = n
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.avg = round(averagem(m1, m2, m3),2)
        Student.student_count += 1
        if self.avg>=90:
            self.grade = 'O'
        elif self.avg <90 and self.avg >=80:
            self.grade = 'A'
        elif self.avg <80 and self.avg >=70:
            self.grade = 'B'
        elif self.avg <70 and self.avg >=60:
            self.grade = 'C'
        elif self.avg <60 and self.avg >=50:
            self.grade = 'D'
        else:
            self.grade = 'F'
    def display(self):
        print(self.stdid,"\t",self.name,"\t",self.marks1,"\t",self.marks2,"\t",self.marks3,"\t",self.avg,"\t",self.grade)
a= Student(1, "AAA", 90, 90, 90)
b= Student(2, "BBB", 70, 70, 70)
c= Student(3, "CCC", 10, 30, 40)
d= Student(4, "DDD", 5, 50, 50)
e= Student(5, "EEE", 56, 57, 58)
print("College Name: ", Student.college_name)
print("Total Students: ", Student.student_count)
print("ID\tName\tSub1\tSub2\tSub3\tAverage\tGrade")
a.display()
b.display()
c.display()
d.display()
e.display()