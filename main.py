import os
def get_file_size(filename):
        return os.path.getsize(filename)
import os
def get_environment_variable(var):
        return os.getenv(var)