import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import platform
def get_os_info():
        return platform.uname()