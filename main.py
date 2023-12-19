import platform
def get_os_info():
        return platform.uname()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)