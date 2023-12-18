import array
def get_array_slice(array, i, j):
        return array[i:j]
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])