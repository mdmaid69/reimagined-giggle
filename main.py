import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import os
def get_environment_variable(var):
        return os.getenv(var)