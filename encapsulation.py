class Employee:

    def __init__(self, fullname, position, status, age):
        self.fullname = fullname
        self.__position = position      #private property
        self.status = status
        self.age = age

    def get_position(self):
        print(self.__position)

