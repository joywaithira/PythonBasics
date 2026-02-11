class Animal:                       #Parent/Super/Base class
    #Attribute - written like variables
    isMammal = True


    #Behaviours - written like functions
    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")



class Cat(Animal):                     #Child/Sub/Derived class
    #the brackets are borrowing hence inheriting
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")



class Horse:
    hasTail = True

    def neigh(self):
        print("Horse is neighing")


    #creating objects
a = Animal()

c = Cat()

h = Horse()


#now call on something by varriable and a dot (a.move)
#to do inheritance your class has to be public which is normally the case in python only

