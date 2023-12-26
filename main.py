n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}