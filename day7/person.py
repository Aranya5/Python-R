class Person:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender=g
class Publication:
    def __init__(self,nr,nb,na):
        self.no_rp = nr
        self.no_book = nb
        self.no_art = na
class Faculty(Person, Publication):
    def __init__(self,n,a,g,nr,nb,na,des,dep):
        Person.__init__(self,n,a,g)
        Publication.__init__(self,nr,nb,na)
        self.desig = des
        self.dept = dep
    def display(self):
        print("Name of faculty:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Designation:",self.desig)
        print("Department:",self.dept)
        print("No of research papers published:",self.no_rp)
        print("No of book chapters published:",self.no_book)
        print("No of articles published:",self.no_art)
n= input("Enter name of faculty: ")
a= int(input("Enter age of faculty: "))
g= input("Enter gender of faculty: ")
nr= int(input("Enter no of research papers published: "))
nb= int(input("Enter no of book chapters published: ")) 
na= int(input("Enter no of articles published: "))
des= input("Enter designation of faculty: ")
dep= input("Enter department of faculty: ")
print()
f= Faculty(n,a,g,nr,nb,na,des,dep)
f.display()