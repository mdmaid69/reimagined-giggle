import array
def convert_array_to_string(array):
        return array.tostring()
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])