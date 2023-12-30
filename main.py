import os
def get_environment_variable(var):
        return os.getenv(var)
def remove_duplicates(lst):
        return list(set(lst))