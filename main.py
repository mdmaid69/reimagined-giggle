import platform
def get_os_info():
        return platform.uname()
import array
def get_bytes_from_array(array):
        return array.tobytes()