import platform
def get_os_info():
        return platform.uname()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)