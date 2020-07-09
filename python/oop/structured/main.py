from student import Student
from department import Department
# from course import Course
# from course import CourseRunning
import course

departments = []
courses = []
courses_running = []
students = []


def open_menu():
    print('Welcome to Xavier School for Gifted Youngsters')
    ans = True

    while ans:
        print("""
        1. Add a Department
        2. Add a Course
        3. Add Course Running
        4. Add Student
        0. Exit/Quit
        """)
        ans = input('Please, select an option: ')
        if ans == '1':
            departments.append(add_department())
            print('\n Department Added')
        elif ans == '2':
            if departments:
                courses.append(add_course(departments))
                print('\n Course Added')
            else:
                print('\n No departments found! Please, add a department first.')
        elif ans == '3':
            print('\n Course Running Added')
        elif ans == '4':
            print('\n Student Added')
        elif ans == '0':
            print('\n Goodbye')
            ans = False
        elif ans != '':
            print('\n Try a valid choice!')


def add_department():
    name = input('Department Name: ')
    code = input('Department Code: ')
    return Department(name, code)


def add_course(department_list):
    description = input('Course Description: ')
    course_code = input('Course Code: ')
    course_credits = input('Course Credits: ')

    for index, department in enumerate(department_list, start=1):
        print(index, '.', department.name)
    dept_index = int(input('Select a department:'))
    return Course(description, course_code, course_credits, department_list[dept_index - 1])


def add_course_running():
    pass


def add_student():
    pass

################################################################
# student1 = Student('Geddy Lee', 2112)
# student2 = Student('Neil Peart', 5150)
#
# department1 = Department('ComIT - BC', 'BC')
# department2 = Department('ComIT - AB', 'AB')
#
# course1 = Course('DevOps', 333, 100, department1)
# course2 = Course('React', 444, 120, department2)
#
# course_running1 = course1.add_running(2020)
# course_running2 = course2.add_running(2019)
#
# student1.enrol(course_running1)
# student1.enrol(course_running2)
#
# # print(vars(student1))x
# student1.show_file()
# student2.show_file()
#
# course_running1.list_students()
# course_running2.list_students()

open_menu()