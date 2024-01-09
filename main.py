text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import os
def get_environment_variable(var):
        return os.getenv(var)