import platform
def get_python_version():
        return platform.python_version()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a