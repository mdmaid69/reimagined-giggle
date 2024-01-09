import os
def get_environment_variable(var):
        return os.getenv(var)
import shutil
def delete_directory(path):
        shutil.rmtree(path)