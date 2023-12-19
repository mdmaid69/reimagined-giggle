import platform
def get_python_version():
        return platform.python_version()
import os
def get_environment_variable(var):
        return os.getenv(var)