import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)