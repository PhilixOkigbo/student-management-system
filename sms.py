class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    def __str__(self):
        return f"NAME:{self.name}\nID: {self.id_number}"
    

class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"STUDENT {super().__str__()}\nDISCIPLINE: {self.major}"


class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"INSTRUCTOR {super().__str__()}\nDEPARTMENT: {self.department}"


class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        self.enrolled_students.remove(student)

    def __str__(self):
        return f"COURSE NAME:{self.course_name}\nCOURSE CODE:{self.course_id}\
            \nENROLLED STUDENTS: {[str(student) for student in self.enrolled_students]}"


class Enrollment:
    def __init__(self, student, course, grade=None):
        self.student = student
        self.course = course
        self.grade = grade

    def assign_grade(self, grade):
        if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.grade = grade
        else:
            raise ValueError(f"Invalid grade: {grade}. Please select from A, B, C, D, E, F.")

    def __str__(self):
        return f"STUDENT: {self.student}\nCOURSE: {self.course}\nGRADE: {self.grade}"






class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    #students
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)
        self.enrollments = [enroll for enroll in self.enrollments if enroll.student != student]
        for course in self.courses:
            if student in course.enrolled_students:
                course.remove_student(student)

    def update_student(self, student, name=None, major=None):
        if name:
            student.name = name
        if major:
            student.major = major

    #instructors
    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)

    def update_instructor(self, instructor, name=None, department=None):
        if name:
            instructor.name = name
        if department:
            instructor.department = department

    #courses
    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)
        self.enrollments = [enroll for enroll in self.enrollments if enroll.course != course]

    def update_course(self, course, course_name=None, course_id=None):
        if course_name:
            course.course_name = course_name
        if course_id:
            course.course_id = course_id

    #Enrollments
    def enroll_student(self, student, course):
        if student not in course.enrolled_students:
            course.add_student(student)
            self.enrollments.append(Enrollment(student, course))

    def assign_grade(self, student, course, grade):
        for enroll in self.enrollments:
            if enroll.student == student and enroll.course == course:
                enroll.assign_grade(grade)
                break

    
    #Retrivals
    def get_students_in_course(self, course):
        return course.enrolled_students

    def get_courses_for_student(self, student):
        return [enroll.course for enroll in self.enrollments if enroll.student == student]






# TESTING THE PROGRAM

print('\n********************** Testing the Person, Instructor, Student and SMS Class ***********************')
#Intialize the Student Management System Class
sms = StudentManagementSystem()


instructor1 = Instructor('Professor Chinedu Okibs', 'T001', 'Economics')
print('\n')
print(instructor1,'\n')

instructor2 = Instructor('Dr. Muna Okibs', 'T002', 'Economics')
print(instructor2,'\n')

student1 = Student('Osita Okibs', 'S001', 'Economics & Statistics')
print(student1,'\n')

student2 = Student('Nnadozie Okibs', 'S002', 'Economics & Statistics')
print(student2,'\n')

student3 = Student('Kamsi Okibs', 'S003', 'Economics & Statistics')
print(student3,'\n')



# Add students and instructors to the system
sms.add_student(student1.name)
sms.add_student(student2.name)
sms.add_instructor(instructor1.name)
sms.add_instructor(instructor2.name)



course1 = Course('Econometrics', 'ECO500')
course2 = Course('Monetary Economics', 'ECO300')

sms.add_course(course1)
sms.add_course(course2)


# Enroll students in courses
sms.enroll_student(student1.name, course1)
sms.enroll_student(student2.name, course2)
sms.enroll_student(student3.name, course2)

sms.assign_grade(student1.name, course1, 'A')
sms.assign_grade(student2.name, course2, 'B')
sms.assign_grade(student3.name, course2, 'B')



# Retrieve and print students in a specific course
students_in_course1 = sms.get_students_in_course(course2)
print(f"Students in {course1.course_name}: {[str(student) for student in students_in_course1]}")



# Retrieve and print courses for a specific student
courses_for_student1 = sms.get_courses_for_student(student1.name)
print(f"Courses for {student1.name}: {[str(course.course_name) for course in courses_for_student1]}\n")




print('\n********************** Testing the Course and Enrollment Class***********************')
# Testing the Course and Enrollment Class
students = Student('Chinedu Okigbo', 'S001', 'Economics & Statistics')
print(students,'\n')

courses = Course('Econometrics', 'ECO500')
courses.add_student('Chinedu')
courses.add_student('Felix')
courses.add_student('Osita')
courses.add_student('Osarobo')
courses.remove_student('Osarobo')
print(courses,'\n')

enrolled = Enrollment(students.name, courses.course_name, 'A')
print(enrolled)

