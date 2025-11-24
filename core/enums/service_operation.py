from enum import Enum


# https://docs.python.org/3/library/enum.html
class ServiceOperation(Enum):
    # Performs the INSERT statement to create a new record in SQL databases.
    CREATE = 1

    # Deletes a specified row in the WHERE clause.
    DELETE = 2

    # Reads the table records based on the primary keynoted within the input parameter.
    READ = 3

    # Executes an UPDATE statement on the table based on the specified primary key for a record within
    # the WHERE clause of the statement
    UPDATE = 4

    # ToString
    def __repr__(self):
        return f"{self.name}"

    # class method
    @classmethod
    def has_value(cls, service_operation):
        # iterate each entry and compare values
        for entry in cls:
            # if same value, return true
            if entry.name.lower() == service_operation.lower():
                return True
        # otherwise false
        return False

    # class method
    @classmethod
    def of_name(cls, service_operation):
        # iterate each entry and compare values
        for entry in cls:
            if entry.name.lower() == service_operation.lower():
                return entry
        # otherwise nothing
        return None


# starting point
if __name__ == '__main__':
    service_operation = ServiceOperation.CREATE
    print(ServiceOperation)
    print(service_operation)
    # has_value()
    print(ServiceOperation.has_value("create"))
    print(ServiceOperation.has_value("Create"))
    print(ServiceOperation.has_value("CREATE"))
    # of_string()
    print(ServiceOperation.of_name("create"))
    print(ServiceOperation.of_name("Create"))
    print(ServiceOperation.of_name("CREATE"))
    print(ServiceOperation.of_name("lakra"))
