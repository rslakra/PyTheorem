class Singleton:
    # Class-level attribute to hold the single instance
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # If no instance exists, create one
            cls.__instance = super().__new__(cls)

        # Always return the same instance
        return cls.__instance


# All "instances" refer to the same object
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True
assert s1 is s2

# Changes to one instance are reflected in the other
s1.data = "Shared Data"
print(s2.data)  # Output: Shared Data
assert s1.data == s2.data
