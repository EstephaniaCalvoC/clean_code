"""
Very advanced Employee management system.
"""
from company import Company
from employee import HourlyEmployee, SalariedEmployee
from role import Role

def main() -> None:
    """Main function."""
    # TODO: Create test for a cmd to handle a CRUD
    # TODO: Create the simple cmd

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_employees(Role.VICEPRESIDENT))
    print(company.find_employees(Role.MANAGER))
    print(company.find_employees(Role.INTERN))
    company.employees[0].pay_employee()
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
