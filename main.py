import platform
def get_os_info():
        return platform.uname()
import shutil
def delete_directory(path):
        shutil.rmtree(path)