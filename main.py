numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}