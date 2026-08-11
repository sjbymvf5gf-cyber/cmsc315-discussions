"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Employee:
    company = "Google"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee {self.name}, ID: {self.employee_id}, Company: {self.company}")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Manager(Employee):
    department_type = "Management"

    def __init__(self, name, employee_id, department, personnel):
        super().__init__(name, employee_id)

        self.department = department
        self.personnel = personnel

    def manage_team(self):
        print(f"{self.name} manages {self.department} team.")

    def display_info(self):
        print(f"Manager Name: {self.name}, Employee ID: {self.employee_id}, Department: {self.department}, Personnel: {self.personnel}, Company: {self.company}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    manager1 = Manager("Alice", "EMP002", "Human Resources", 5)
    manager2 = Manager("Bob", "EMP003", "IT", 3)

    print("Manager at company:", Manager.company)

    print("Manager 1 Company:", manager1.company)

    manager1.office_location = "Floor 3"

    print("Manager 1 Namespace:")
    print(manager1.__dict__)
    print("Manager 2 Namespace:")
    print(manager2.__dict__)

    print("Employee class namespace:")
    print(Employee.__dict__)
    print("Manager class namespace:")
    print(Manager.__dict__)
    print("Manager 1 Information:")
    print(manager1.display_info())
    print("Manager 2 Information:")
    print(manager2.display_info())
    print("Manager 1 Additional Information:")
    print(manager1.manage_team())

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")
    original_employee = {"Name": "Charlie", "Employee": "EMP005", "Skills": {"Technical": ["Python", "SQL"], "Soft": ["Communication", "Networking"]}}

    shallow_copy = copy(original_employee)
    deep_copy = deepcopy(original_employee)

    original_employee["Skills"]["Technical"].append("Java")

    print("Original employee copy:")
    print(original_employee)
    print("Shallow copy:")
    print(shallow_copy)
    print("Deep copy:")
    print(deep_copy)

    """In Shallow copy, you create a new object but can add items(elements) while referencing the original list,
    whereas in Deep copy it duplicates the original object only."""

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")
    print("\nTODO: Create and test your parent object")

    print("Employee object: ")
    employee = Employee("David", "EMP001")
    employee.display_info()
    print("\nTODO: Create and test your child object")
    print("Manager object: ")
    manager = Manager("Emma", "EMP006", "Salary", 6)

    print(manager.display_info())

    print(manager.manage_team())

    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()