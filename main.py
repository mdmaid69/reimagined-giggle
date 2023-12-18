import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import platform
def get_os_info():
        return platform.uname()