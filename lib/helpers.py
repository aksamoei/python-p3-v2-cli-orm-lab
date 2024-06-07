from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    employee_name = input("Enter employee's name: ")
    employee = Employee.find_by_name(employee_name)
    if employee:
        print(employee)
    else:
        print(f"{employee_name} was not found in our Employees")


def find_employee_by_id():
    employee_id = int(input("Enter the employee's id: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        print(employee)
    else:
        print(f"The id {employee_id} doesn't match any of the employees")

def create_employee():
    employee_name = input("Enter the employee's name: ")
    employee_job_title = input("Enter the employee's job title: ")
    employee_department_id = int(input("Enter the employee's department id: "))

    employee = Employee.create(employee_name, employee_job_title, employee_department_id)
    if employee:
        print(employee)
    else:
        print("Unable to create the employee")


def update_employee():
    employee_id = int(input("Enter the employee's id: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        try:
            employee.name = input("Enter the employee's name: ")
            employee.job_title = input("Enter the job title: ")
            employee.department_id = int(input("Enter the emplyee's department id: "))
            employee.update()
            print(f"Succesfully updated, {employee}")
        except Exception as error:
            print(f"Error updating the employee, {error}")
    else:
        print(f"Unable to update to absence of an employee with id {employee_id}")

def delete_employee():
    employee_id = int(input("Enter the employees id: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        employee.delete()
        print(f"Succesfully deleted employee with id {employee_id}.")
    else:
        print(f"Didn't find employee with id {employee_id}")


def list_department_employees():
    department_id = int(input("Enter the department's ID: "))
    department = Department.find_by_id(department_id)
    if department:
        department_employees = department.employees()
        for employee in department_employees:
            print(employee)
    else:
        print(f"Unable to find department with id {department_id} and its employees")
