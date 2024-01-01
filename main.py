import os
def get_environment_variable(var):
        return os.getenv(var)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)