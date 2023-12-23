import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)