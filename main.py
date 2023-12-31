import os
def get_environment_variable(var):
        return os.getenv(var)
def greet(name):
        print(f"Hello, {name}!")