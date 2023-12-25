import array
def get_array_as_bytes(array):
        return bytes(array)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])