import platform
def get_python_version():
        return platform.python_version()
import shutil
def delete_directory(path):
        shutil.rmtree(path)