from student_management import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Adding Students
    sms.add_student("Alice", "alice@example.com")
    sms.add_student("Bob", "bob@example.com")

    # Adding Courses
    sms.add_course("Mathematics")
    sms.add_course("Physics")

    # Enrolling Students in Courses
    sms.enroll_student_in_course("1", "1")  # Alice enrolls in Mathematics
    sms.enroll_student_in_course("2", "2")  # Bob enrolls in Physics

    # Assigning Grades
    sms.assign_grade("1", "1", 85)  # Assigns a grade of 85 to Alice in Mathematics
    sms.assign_grade("2", "2", 90)  # Assigns a grade of 90 to Bob in Physics

    # Calculating GPA
    sms.calculate_gpa("1")  # Calculates GPA for Alice
    sms.calculate_gpa("2")  # Calculates GPA for Bob
