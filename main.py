import glob
def find_files(pattern):
        return glob.glob(pattern)
import os
def get_environment_variable(var):
        return os.getenv(var)