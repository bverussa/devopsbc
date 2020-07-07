class Person:

    # Class Attributes
    specie = 'human being'

    # Constructor
    def __init__(self, name, age, program, role):
        self.name = name
        self.age = age
        self.program = program
        self.role = role

    def show_person(self):
        print(self.name, 'is', self.age, 'years old', self.specie + '.', 'ComIT -', self.program, 'as', self.role + '.')


student_1 = Person('Mike', 45, 'DevOps', 'Student')
student_2 = Person('John', 41, 'DevOps', 'Student')
coordinator_1 = Person('Bruce', 32, 'DevOps', 'Coordinator')
instructor_1 = Person('Emerson', 71, 'DevOps', 'Instructor')

student_1.show_person()
student_2.show_person()
coordinator_1.show_person()
instructor_1.show_person()
