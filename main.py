import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import os
def get_environment_variable(var):
        return os.getenv(var)