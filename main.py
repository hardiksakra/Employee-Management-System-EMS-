used_id = set()
employeees = {}

def add_employee():

    emp_id = input("Enter Employee ID: ")

    if emp_id in used_id:
        print("Employee ID already exists. Please try again.")
        return
    used_id.add(emp_id)

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))

    employeees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    print("Employee added successfully!")

    


def view_employees():
    if not employeees:
        print("No employees available.")
        return

    for emp_id, details in employeees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    if emp_id in employeees:
        details = employeees[emp_id]
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
    else:
        print("Employee not found.")
def main():
    print("Welcome to the Employee Management System!")
    

    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                add_employee()
            case '2':
                view_employees()
            case '3':
                search_employee()
            case '4':
                print("Thank you for using the Employee Management System. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
