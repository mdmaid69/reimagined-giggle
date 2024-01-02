import random
print(random.randint(0, 100))
import os
def get_environment_variable(var):
        return os.getenv(var)