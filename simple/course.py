#A Student class has attributes like name and age.A Course class has attributes like course_name and instructor.Use aggregation to associate multiple courses with a student.

class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []  # List to store enrolled courses

    def enroll_in_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        return [f"{course.course_name} taught by {course.instructor}" for course in self.courses]

def main():
    print("Welcome to the Student Enrollment System!")
    
    
    student_name = input("Enter the student's name: ")
    student_age = int(input("Enter the student's age: "))
    student = Student(student_name, student_age)

    
    while True:
        print("\nAdding a new course:")
        course_name = input("Enter the course name: ")
        instructor_name = input("Enter the instructor's name: ")
        course = Course(course_name, instructor_name)
        student.enroll_in_course(course)

        add_another = input("Do you want to add another course? (yes/no): ").strip().lower()
        if add_another != 'yes':
            break
    
    
    print(f"\nStudent: {student.name}, Age: {student.age}")
    print("Enrolled Courses:")
    for course in student.list_courses():
        print(course)

if __name__ == "__main__":
    main()
