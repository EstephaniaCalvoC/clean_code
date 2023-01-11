"""Class to handle a company objet"""
from typing import List, Dict
from role import Role
from employee import Employee
from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def add_employee(self, employee_info):
        # TODO: Write record in a CV file or make a post
        pass

    @abstractmethod
    def get_employee_by_role(self, role):
        # TODO: Query or find the employees with the indicate role
        pass

    @abstractmethod
    def get_all_employees(self):
        # TODO: Query to get all the employees
        pass

    @abstractmethod
    def load(self, csv_file):
        # TODO: Load employees from a CSV file
        pass


class DataFile(DataManager):
    employees: Dict[Employee] = dict()

    def __init__(self, **kwargs):
        self.csv_file = kwargs.get("csv_file")

    def add_employee(self, employee_info):
        employee_id = employee_info.pop("id")
        # TODO: Add to the csv file
        self.employees.update({employee_id: employee_info})
        return employee_id

    def get_employee_by_role(self, role):
        return [employee
                for employee in self.employees.values()
                if employee.role is role]

    def get_all_employees(self):
        return self.employees

    def load(self, csv_file):
        pass

    def get_employee(self):
        pass

    def update_employee(self):
        pass

    def delete_employee(self):
        pass


class Company:
    """Represents a company with employees."""

    def __init__(self, data_manager) -> None:
        self.data_manager: DataManager = data_manager

    def get_employees(self):
        self.data_manager.get_all_employees()

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.data_manager.add_employee(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role."""
        return self.data_manager.get_employee_by_role(role)

    def load_employees(self, csv_file):
        return self.data_manager.load(csv_file)
