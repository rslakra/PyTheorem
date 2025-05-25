from core.enums import BaseEnum


# Define Weekday Enum
class WeekDaysEnum(BaseEnum):
    """WeekDay Enum represents the days of the week. For readability, add constants in Alphabetical order."""
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
    WEEKEND = SATURDAY | SUNDAY

    # add a method to return the weekday from the date
    # @param date
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

    # add a method to return the today's weekday.
    @classmethod
    def today(cls):
        return cls.from_date(date.today())
