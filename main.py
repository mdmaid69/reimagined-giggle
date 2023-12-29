n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}