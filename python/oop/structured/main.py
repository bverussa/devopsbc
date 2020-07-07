from student import Student
from department import Department
from course import Course

student1 = Student('Mike', 1234)
department1 = Department('ComIT - BC', 'BC')
course1 = Course('DevOps', 333, department1)

print(vars(course1))
