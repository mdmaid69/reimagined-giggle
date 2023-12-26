n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}