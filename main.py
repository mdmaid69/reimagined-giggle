import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_volume(length, width, height):
        return length * width * height