class Course:

    def __init__(self, description, course_code, course_credits, department):
        self.description = description
        self.course_code = course_code
        self.course_credits = course_credits
        self.department = department
        self.department.add_course(self)
        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]

class CourseRunning:

    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        if self.students:
            for student in self.students:
                print('List of Students of Course', self.course.description)
                print('-' * 40)
                print(student.name)
        else:
            print('No students enrolled')