import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])