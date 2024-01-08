import platform
def get_python_version():
        return platform.python_version()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()