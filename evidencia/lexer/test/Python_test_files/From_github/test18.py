class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        total = sum(self.grades)
        return total / len(self.grades) if len(self.grades) > 0 else 0

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_average_grade(self):
        total = 0
        num_students = len(self.students)
        for student in self.students:
            total += student.calculate_average()
        return total / num_students if num_students > 0 else 0
    
    def get_maximum_grade(self):
        max_grade = 0
        for student in self.students:
            max_grade = max(max_grade, max(student.grades))
        return max_grade
    
    def get_minimum_grade(self):
        min_grade = 100
        for student in self.students:
            min_grade = min(min_grade, min(student.grades))
        return min_grade
    
    def sort_students_by_average_grade(self):
        sorted_students = sorted(self.students, key=lambda student: student.calculate_average(), reverse=True)
        return sorted_students
    
    def get_students_with_highest_average_grade(self, num_students):
        sorted_students = self.sort_students_by_average_grade()
        return sorted_students[:num_students]
    
    def get_students_with_lowest_average_grade(self, num_students):
        sorted_students = self.sort_students_by_average_grade()
        return sorted_students[-num_students:]

# Create students
student1 = Student("John Doe", 12345)
student2 = Student("Jane Smith", 67890)
student3 = Student("David Johnson", 54321)

# Create a course
course = Course("Mathematics")

# Add students to the course
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# Add grades for each student
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student2.add_grade(92)
student2.add_grade(88)
student2.add_grade(95)

student3.add_grade(80)
student3.add_grade(85)
student3.add_grade(90)

# Calculate and display average grade for each student
for student in course.students:
    average_grade = student.calculate_average()
    print(f"Student: {student.name} (ID: {student.id})")
    print(f"Average Grade: {average_grade}\n")

# Calculate and display average grade for the course
average_course_grade = course.get_average_grade()
print(f"Course: {course.name}")
print(f"Average Course Grade: {average_course_grade}")

# Calculate and display maximum grade for the course
maximum_grade = course.get_maximum_grade()
print(f"Maximum Grade in the Course: {maximum_grade}")

# Calculate and display minimum grade for the course
minimum_grade = course.get_minimum_grade()
print(f"Minimum Grade in the Course: {minimum_grade}")

# Sort students by average grade and display
sorted_students = course.sort_students_by_average_grade()
print("Students sorted by Average Grade:")
for student in sorted_students:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")

# Get students with the highest average grade and display
num_students_highest_grade = 2
students_highest_grade = course.get_students_with_highest_average_grade(num_students_highest_grade)
print(f"\nStudents with the Highest Average Grade ({num_students_highest_grade}):")
for student in students_highest_grade:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")

# Get students with the lowest average grade and display
num_students_lowest_grade = 1
students_lowest_grade = course.get_students_with_lowest_average_grade(num_students_lowest_grade)
print(f"\nStudents with the Lowest Average Grade ({num_students_lowest_grade}):")
for student in students_lowest_grade:
    print(f"Student: {student.name} (ID: {student.id}), Average Grade: {student.calculate_average()}")
