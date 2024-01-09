import os
def get_environment_variable(var):
        return os.getenv(var)
import glob
def find_files(pattern):
        return glob.glob(pattern)