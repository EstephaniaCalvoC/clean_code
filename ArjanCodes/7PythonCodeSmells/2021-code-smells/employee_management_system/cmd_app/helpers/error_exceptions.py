"""Custo error for the Employeer Management System"""

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
