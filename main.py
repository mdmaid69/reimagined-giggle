for i in range(10): print(i)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}