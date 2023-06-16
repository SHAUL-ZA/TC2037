class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def update_student(self, student, name, age, grade):
        student.name = name
        student.age = age
        student.grade = grade

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        print("== Student Registry ==")
        for student in self.students:
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print("---------------------")

def display_menu():
    print("== Student Registry Menu ==")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Search Student by ID")
    print("6. Exit")

def run_student_registry():
    student_registry = StudentRegistry()

    while True:
        display_menu()
        option = input("Select an option: ")

        if option == "1":
            student_id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            grade = input("Enter the student grade: ")
            student = Student(student_id, name, age, grade)
            student_registry.add_student(student)
            print("Student added successfully.")

        elif option == "2":
            student_id = input("Enter the student ID to remove: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                student_registry.remove_student(student)
                print("Student removed successfully.")
            else:
                print("Student not found.")

        elif option == "3":
            student_id = input("Enter the student ID to update: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                name = input("Enter the new name: ")
                age = input("Enter the new age: ")
                grade = input("Enter the new grade: ")
                student_registry.update_student(student, name, age, grade)
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif option == "4":
            student_registry.display_students()

        elif option == "5":
            student_id = input("Enter the student ID to search: ")
            student = student_registry.get_student_by_id(student_id)
            if student:
                print("Student found:")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
            else:
                print("Student not found.")

        elif option == "6":
            print("Exiting the Student Registry.")
            break

        else:
            print("Invalid option. Please select a valid option.")

run_student_registry()
