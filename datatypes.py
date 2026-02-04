#This are different datatypes
age = 17    #integer
weight = 45.79     #float
greeting = "Hello there!"     #string
isMammal = True   #boolean

#Data structures - are multiple elements in one variable
fruits = ["Banana", "Mango", "Cherry"]    #List  - is ordered and changeable and can have different datatypes
courses = ["MIT", "DataScience", "CyberSecurity"]     #Array - same as a list but can only carry values of the same data types
cars = ("Ford", "G wagon", "Mazda", "Mitsubishi")  #Tuple - elements are ordered but unchangeable
countries = {"Tanzania", "India", "Italy"}    #Set - elements are unordered and unchangeable
student = {
    "firstname" : "Jeff",
    "course" : "MIT",
    "age" : 17,
    "nationality" : "Kenyan"
}     #Dictionary - key value pair



print("Student is", age, "years old")
print(weight)
print("Is animal a mammal? :", isMammal)
print(fruits)
print(courses[1])
print(countries)




#Typecasting - changing one data type to another
print(float(age))
print(int(weight))
