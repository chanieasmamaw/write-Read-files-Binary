class StudentDetails:
    def __init__(self, full_name, date_of_birth, gender, address, phone_numbers, email, student_id, enrollment_date, current_grade, major_studies, mentor_name, gpa):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone_numbers = phone_numbers
        self.email = email
        self.student_id = student_id
        self.enrollment_date = enrollment_date
        self.current_grade = current_grade
        self.major = major_studies
        self.advisor = mentor_name
        self.gpa = gpa

    def print_student_info(self):
        print("\nStudent Information:")
        print(f"Full Name: {self.full_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")
        print(f"Phone Numbers: {', '.join(self.phone_numbers)}")
        print(f"Email Address: {self.email}")
        print(f"Student ID: {self.student_id}")
        print(f"Enrollment Date: {self.enrollment_date}")
        print(f"Current Grade/Class: {self.current_grade}")
        print(f"Major/Field of Study: {self.major}")
        print(f"Academic Advisor: {self.advisor}")
        print(f"GPA: {self.gpa}")

def main():
    number_of_students = int(input("Enter the number of students: "))

    students = []
    for _ in range(number_of_students):
        full_name = input("Enter full name: ")
        date_of_birth = input("Enter date of birth (dd/mm/yyyy): ")
        gender = input("Enter gender: ")
        address = input("Enter address: ")
        phone_numbers = input("Enter phone numbers (comma separated): ").split(',')
        email = input("Enter email address: ")
        student_id = input("Enter student ID: ")
        enrollment_date = input("Enter enrollment date (dd/mm/yyyy): ")
        current_grade = input("Enter current grade/class: ")
        major_studies = input("Enter major/field of study: ")
        mentor_name = input("Enter academic advisor's name: ")
        gpa = input("Enter GPA: ")

        student = StudentDetails(
            full_name,
            date_of_birth,
            gender,
            address,
            phone_numbers,
            email,
            student_id,
            enrollment_date,
            current_grade,
            major_studies,
            mentor_name,
            gpa)
        

        students[student_id] = student

    for student_id, student in students.items():
        student.print_student_info()

if __name__ == "__main__":
    main()
