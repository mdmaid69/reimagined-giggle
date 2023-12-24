import platform
def get_os_info():
        return platform.uname()
import glob
def find_files(pattern):
        return glob.glob(pattern)