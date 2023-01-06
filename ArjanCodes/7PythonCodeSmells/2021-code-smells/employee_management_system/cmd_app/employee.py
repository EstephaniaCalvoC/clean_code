"""Classes for every kind of employee"""
from dataclasses import dataclass
from role import Role
from helpers.constants import FIXED_VACATION_DAYS_PAYOUT
from helpers.error_exceptions import InsuficentHolidaysToPayoutError, InsuficentHolidaysToTakeError
from abc import ABC, abstractmethod

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