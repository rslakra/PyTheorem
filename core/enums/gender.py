from enum import Enum


# https://docs.python.org/3/library/enum.html
class Gender(Enum):
    FEMALE = 1
    MALE = 2
    NIL = 0

    # ToString
    def __repr__(self):
        return f"{self.name}"

    # class method
    @classmethod
    def has_value(cls, gender):
        for entry in cls:
            if entry.name.lower() == gender.lower():
                return True

        return False

    # class method
    @classmethod
    def of_name(cls, gender):
        for entry in cls:
            if entry.name.lower() == gender.lower():
                return entry

        return Gender.NIL


# starting point
if __name__ == '__main__':
    gender = Gender.NIL
    print(Gender)
    print(gender)
    print(Gender.has_value("male"))
    print(Gender.has_value("ale"))
    print(Gender.of_name("male"))
