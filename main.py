import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import platform
def get_python_version():
        return platform.python_version()