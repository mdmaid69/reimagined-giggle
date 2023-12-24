import os
def change_working_directory(path):
        os.chdir(path)
import os
def get_environment_variable(var):
        return os.getenv(var)