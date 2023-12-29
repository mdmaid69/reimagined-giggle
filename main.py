import sys
print(sys.version)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)