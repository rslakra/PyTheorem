from enum import unique

from core.enums import BaseEnum


class ShapeEnum(BaseEnum):
    """Shape Enum defines various shapes. For readability, add constants in Alphabetical order."""
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3
    DIAMOND_ALIAS = 2

    @classmethod
    def all_shapes(cls):
        """
        Note that the aliases Shape.DIAMOND_ALIAS and WeekDay.WEEKEND aren’t shown.
        The special 'attribute __members__' is a read-only ordered mapping of names to members.
        It includes all names defined in the enumeration, including the aliases:
        all_shapes = list([name, entry for name, entry in Shape.__members__().items()])

        # The special attribute __members__ is a read-only ordered mapping of names to members.

        :return:
        """
        # return cls(list(Shape.__members__.items()))
        # returns (name, Enum) as list
        return list(cls.__members__.items())


# Ensuring unique enumeration values
@unique
class UniqueShapeEnum(BaseEnum):
    """Unique Shape Enum defines various shapes. For readability, add constants in Alphabetical order."""
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3
