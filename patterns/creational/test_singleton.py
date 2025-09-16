# Main application file
# test_singleton.py

from patterns.creational.singleton_module import instance

# Access the same instance from anywhere by importing the module
instance1 = instance
instance2 = instance

print(instance1 is instance2)  # Output: True
assert instance1 is instance2

# Changes to one instance are reflected in the other
print(instance2.data)  # Output: Shared Data
assert instance1.data == instance2.data
