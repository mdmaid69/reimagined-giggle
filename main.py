import array
def get_array_as_frozenset(array):
        return frozenset(array)
n = 10
print("Powers of 2:", [2**x for x in range(n)])