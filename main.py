import os
def get_environment_variable(var):
        return os.getenv(var)
i = 0
while i < 5:
        print(i)
        i += 1