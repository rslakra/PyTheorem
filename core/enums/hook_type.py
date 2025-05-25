from core.enums import BaseEnum


class HookType(BaseEnum):
    """HookType Enum"""
    BEFORE_ALL = 'before_all'  # Runs once before all tests.
    AFTER_ALL = 'after_all'  # Runs once after all tests.
    BEFORE_FEATURE = 'before_feature'  # Runs before each feature file is tested.
    AFTER_FEATURE = 'after_feature'  # Runs after each feature file has been tested.
    BEFORE_SCENARIO = 'before_scenario'  # Runs before each scenario.
    AFTER_SCENARIO = 'after_scenario'  # Runs after each scenario.
    BEFORE_STEP = 'before_step'  # Runs before each step.
    AFTER_STEP = 'after_step'  # Runs before each step.
    BEFORE_TAG = 'before_tag'  # Runs before each tag.
    AFTER_TAG = 'after_tag'  # Runs before each tag.


print()
print(HookType)
print(HookType.names())
print()
for hook_type in HookType.names():
    print(f"hook_type={hook_type}, type={type(hook_type)}")
print()
