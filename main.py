import array
def get_array_as_frozenset(array):
        return frozenset(array)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])