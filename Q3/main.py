from employee_management import EmployeeManagementSystem

if __name__ == "__main__":
    ems = EmployeeManagementSystem()

    # Adding Employees
    ems.add_employee("Ruthra", "ruthra@example.com", "Software Engineer", 60000)
    ems.add_employee("Rutrhavarshan", "ruthravarshan.s@example.com", "security analyst", 75000)
    ems.add_employee("Varshan", "varshan@gmail.com", "Data Scientist",90000)

    # Updating Employee Information
    ems.update_employee("1", job_title="Senior Software Engineer", base_salary=70000)

    # Adding Performance Metrics
    ems.add_performance_metric("1", "Project Success", 9.0)
    ems.add_performance_metric("2", "Team Leadership", 8.5)
    ems.add_performance_metric("3", "Quality Reports", 9.5)

    # Calculating Salaries with Bonus
    ems.calculate_salary("1", performance_weight=1000)
    ems.calculate_salary("2", performance_weight=1200)
    ems.calculate_salary("3", performance_weight=2200)
