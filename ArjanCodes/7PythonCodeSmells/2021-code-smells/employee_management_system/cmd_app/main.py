#!/usr/bin/env python3
"""
Very advanced Employee management system.
"""
from company import Company
from employee import HourlyEmployee, SalariedEmployee
from role import Role


import cmd, sys


class EmployeeManagementSystem(cmd.Cmd):
    intro = "Welcome to the very advance Employee management system."
    prompt = "(EMS) "

    # --- Company commands ---#

    def do_create_company(self, arg):
        """Create a company"""
        print(f"Creating a company: {arg}")

    def do_close(self, arg):
        """Finish the program"""
        print("Closing the EMS")
        return True


def main() -> None:
    """Main function."""
    # TODO: Create test for a cmd to handle a CRUD
    # TODO: Create the simple cmd

    EmployeeManagementSystem().cmdloop()

    # company = Company()
    #
    # company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    # company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    # company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))
    #
    # print(company.find_employees(Role.VICEPRESIDENT))
    # print(company.find_employees(Role.MANAGER))
    # print(company.find_employees(Role.INTERN))
    # company.employees[0].pay_employee()
    # company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
