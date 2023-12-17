def find_difference(list1, list2):
        return set(list1) - set(list2)
import os
def get_environment_variable(var):
        return os.getenv(var)