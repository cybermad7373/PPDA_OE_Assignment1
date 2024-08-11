from student_management import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Adding Students
    sms.add_student("Ruthra","ruthravarshan@gmail.com")
    sms.add_student("Ruthravarshan","ruthra@gmail.com")
    sms.add_student("Varshan","varshan123@gmail.com")

    # Adding Courses
    sms.add_course("Data Science")
    sms.add_course("Networking")
    sms.add_course("Data Structure")


    # Enrolling Students in Courses
    sms.enroll_student_in_course("1", "1")  # Ruthra enrolls in Data Science
    sms.enroll_student_in_course("2", "2")  # Ruthravarshan enrolls in Networking
    sms.enroll_student_in_course("3","3")   # varshan enrolls in Data Structure
    sms.enroll_student_in_course("2", "3")  # Ruthravarshan also enrolls in Data Structures

    # Assigning Grades
    sms.assign_grade("1", "1", 85)  # Assigns a grade of 85 to Ruthra in Data Science
    sms.assign_grade("2", "2", 90)  # Assigns a grade of 90 to Ruthravarshanob in Networking
    sms.assign_grade("3", "3", 84)  # Assigns a grade of 84 to varshan in Data Structure
    sms.assign_grade("2", "3", 67)

    # Calculating GPA
    sms.calculate_gpa("1")  # Calculates GPA for Ruthra
    sms.calculate_gpa("2")  # Calculates GPA for Ruthravarshan
    sms.calculate_gpa("3")  # Calculates GPA for varshan
