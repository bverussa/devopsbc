class Department:

    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, course):
        self.courses[course.course_code] = course
        return self.courses[course.course_code]
