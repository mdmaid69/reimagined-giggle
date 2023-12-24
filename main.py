import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import os
def get_environment_variable(var):
        return os.getenv(var)