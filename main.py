import array
def get_array_as_int(array):
        return int(array[0])
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])