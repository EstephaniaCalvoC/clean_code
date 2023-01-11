#!/usr/bin/env python3
"""
Very advanced Employee management system.
"""
# from company import Company
# from employee import HourlyEmployee, SalariedEmployee
# from role import Role


import cmd, sys


class EmployeeManagementSystem(cmd.Cmd):
    intro = "Welcome to the very advance Employee management system."
    prompt = "(EMS) "
    company = None

    def parser(self, arg):
        pass

    def do_load(self, arg):
        # TODO: Be able to load a csv file as db with the name of the company, every row is an employee. New actio do_load

        # Load the employees in a given CSV file, either in DataFile or DataBase
        # Use self.company.load(csv_file)
        pass


    # --- Company commands ---#

    def do_create_company(self, arg):
        """Create a company"""
        # TODO: Check if already exist a file, if it does suggest use load or other location

        # TODO: Pass parser to other function
        company_name, location = arg.split(", ")

        file_name = "_".join(company_name.lower().split()) + ".csv"
        file_path = f'{location}/{file_name}'
        with open(file_path, "w") as f:
            pass

        # TODO: Create the object company, use self.company = Company(DataManager), the DataManager depends of the Environment

        print(f"Success: The company {company_name} was created successfully in {location} as {file_name}")

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
