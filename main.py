import array
def convert_array_to_bytes(array):
        return array.tobytes()
import platform
def get_os_info():
        return platform.uname()