import array
def get_array_as_tuple(array):
        return tuple(array)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])