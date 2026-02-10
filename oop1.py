#making classes that don't have fixed values but instead you create the
#variables yourself and use parameters then when called on you input values

class Employee:

    #Attributes
    def __init__(self, fullname, position, status, age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print(self.fullname, "is working")

employee1 = Employee("Ken Mwenda", "MD", "Married", 40)
print(employee1.fullname, employee1.position, employee1.status, employee1.age)
employee1.work()

employee2 = Employee("Jean Kamau", "Programes Manager", "Single", 34)
print(employee2.fullname, employee2.position, employee2.status, employee2.age)
employee1.work()

employee3 = Employee("Mark Joe", "Lecturer", "Single", 45)




