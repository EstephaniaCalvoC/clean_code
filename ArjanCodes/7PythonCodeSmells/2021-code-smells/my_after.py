"""
Very advanced Employee management system.
"""

from dataclasses import dataclass
from typing import List
from enum import Enum, auto

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class Role(Enum):
    """Employee roles types"""
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            # check that there are enough vacation days left for a payout
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"You don't have enough holidays left over for a payout.\
                        Remaining holidays: {self.vacation_days}."
                )
            try:
                self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
                print(f"Paying out a holiday. Holidays left: {self.vacation_days}")
            except Exception:
                # this should never happen
                pass
        else:
            if self.vacation_days < 1:
                raise ValueError(
                    "You don't have any holidays left. Now back to work, you!"
                )
            self.vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    amount: int = 10


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role."""
        return [employee for employee in self.employees if employee.role == role]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.name} a hourly rate of \
                ${employee.hourly_rate} for {employee.amount} hours."
            )


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_employees(Role.VICEPRESIDENT))
    print(company.find_employees(Role.MANAGER))
    print(company.find_employees(Role.INTERN))
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()
