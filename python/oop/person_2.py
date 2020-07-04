class Person:

    # Class Attributes
    specie = 'human being'

    # Constructor
    def __init__(self, name, age, program, role):
        self.name = name
        self.age = age
        self.program = program
        self.role = role
        self.show_person()

    def show_person(self):
        print(self.name, 'is', self.age, 'years old', self.specie + '.',
              'ComIT -', self.program, 'as', self.role + '.')


class Employee(Person):

    # Constructor
    def __init__(self, name, age, program, role, wage):
        self.wage = wage
        Person.__init__(self, name, age, program, role)

    def show_person(self):
        print(self.name, 'is', self.age, 'years old', self.specie + '.', 'ComIT -', self.program, 'as',
              self.role + '.', 'Wage: $', self.wage)


student_1 = Person('Mike', 45, 'DevOps', 'Student')
student_2 = Person('John', 41, 'DevOps', 'Student')
coordinator_1 = Employee('Bruce', 32, 'DevOps', 'Coordinator', 2000)
instructor_1 = Employee('Emerson', 71, 'DevOps', 'Instructor', 10000)
