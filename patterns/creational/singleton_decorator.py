def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:

    def __init__(self, db_name):
        self.db_name = db_name
        print(f"Creating database connection to {self.db_name}...")


# Both variables reference the same object
db1 = DatabaseConnection("mydatabase")
db2 = DatabaseConnection("mydatabase")

print(db1 is db2)  # Output: True
assert db1 is db2

# Changes to one instance are reflected in the other
db1.db_name = "Shared Data"
print(db2.db_name)  # Output: Shared Data
assert db1.db_name == db2.db_name
