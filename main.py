print([x**2 for x in range(10)])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}