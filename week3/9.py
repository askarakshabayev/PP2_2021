class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def show(self):
        print(f'{self.name} - {self.surname}')

class Subject:
    pass


class Student(Person): # Person
    def __init__(self, name, surname, gpa, faculty):
        super().__init__(name, surname) # Person init
        self.gpa = gpa
        self.faculty = faculty

    def show(self):
        super().show()
        print(f'{self.gpa} - {self.faculty}')

a = Student("Aaa", "Bbb", 3.9, "FIT") # a.name, a.surname (Person), a.gpa, a.faculty (Student -> Person)
a.show()
b = Student("Bbb", "Ccc", 4.0, "FOGI")
b.show()

# a = Student("Aaa", "Bbb")
# a.show()