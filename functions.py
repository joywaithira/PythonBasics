#Functions/Methods - a block of code used to perform a task
#Standard-library functions(inbuilt functions) - they already exist
y = max (45, 78, 89, 56, 90, 24, 879, 765, 7)
print("The maximum number is", y)


x = min (79, 45, 67, 384, 9, 37, 3, 4859, 940)
print("The minimum number is", x)

print()

#User-defined functions
def name():
    print("Maryjoy")

name()     #calling a function

print()

def add():
    print(10+20)

add()

print()

#Parameters/Variable - inside the brackets of a function
#Arguments/Values - values passed when calling a function
def dog(name, breed, age) :
    print (name, breed, age)

dog("Bob", "German Shepherd", 4)
dog("Mary", "Chihuahua", 2)
dog("Peter", "Siberian Husky", 5)






def ppl(fullname, position, gender, age):
    print (fullname, position, gender, age)

print()

ppl("Ann", "CEO", "Female", 40)
ppl("Kyle", "Opperations Manager", "Male", 30)
ppl("Steve", "Secretary", "Male", 25)
ppl("Angie", "Manager", "Female", 29)
ppl("Jasmine", "Accountant", "Female", 32)
