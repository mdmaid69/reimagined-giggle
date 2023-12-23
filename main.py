import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import platform
def get_python_version():
        return platform.python_version()