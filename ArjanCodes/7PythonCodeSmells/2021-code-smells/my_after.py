"""
Very advanced Employee management system.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from enum import Enum, auto

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class InsuficentHolidaysToPayoutError(Exception):
    """Custom error that is raised when the employee has not enoght holidays to payout"""

    def __init__(self, requested_days: int, remaining_days: int) -> None:
        self.requested_days = requested_days
        self.remaining_day = remaining_days
        self.message = f"You don't have enough holidays left over for a payout.\
                    Remaining holidays: {remaining_days}."
        super.__init__(self.message)


class InsuficentHolidaysToTakeError(Exception):
    """Custom error that is raised when the employee has not enoght holidays to take"""
    
    message = "You don't have any holidays left. Now back to work, you!"
    
    def __init__(self) -> None:
        super.__init__(self.message)


class Role(Enum):
    """Employee roles types"""
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 25

    def payout_holiday(self) -> None:
        """Let the employee pay out 5 holidays"""
        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise InsuficentHolidaysToPayoutError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days)
        
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")
        

    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday"""
        if self.vacation_days < 1:
            raise InsuficentHolidaysToTakeError()
        
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    @abstractmethod
    def pay_employee(self)-> None:
        """Method to pay an employee"""
        pass


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate_dollars: float = 50
    hours_worked: int = 10

    def pay_employee(self) -> None:
        """Pay a hourly employee."""
        print(
                f"Paying employee {self.name} a hourly rate of \
                ${self.hourly_rate_dollars} for {self.hours_worked} hours."
            )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def pay_employee(self) -> None:
        """Pay a salary employee."""
        print(
                f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
            )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role."""
        return [employee for employee in self.employees if employee.role is role]


def main() -> None:
    """Main function."""

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
