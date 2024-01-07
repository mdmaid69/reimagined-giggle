import os
def get_environment_variable(var):
        return os.getenv(var)
import re
print(re.match("h.*o", "hello world"))