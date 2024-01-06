import array
def convert_array_to_bytes(array):
        return array.tobytes()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])