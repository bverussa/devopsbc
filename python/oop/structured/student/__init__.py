class Student:

    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)

    def show_file(self):
        print('Student Name:', self.name)
        print('Student #:', self.student_number)
        print('Enrolled Courses:')
        print('-' * 40)

        if self.classes:
            for enrolled in self.classes:
                print('   Course:', enrolled.course.description, '-', enrolled.course.course_code)
                print('   Credits:', enrolled.course.course_credits)
                print('   Department:', enrolled.course.department.name)
                print('   Year:', enrolled.course.runnings[0].year)
                print('='*30)
        else:
            print('No courses')
