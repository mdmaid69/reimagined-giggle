n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}