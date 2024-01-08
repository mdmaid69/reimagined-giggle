text = "Hello, world!"
print("Words:", len(text.split()))
import os
def get_environment_variable(var):
        return os.getenv(var)