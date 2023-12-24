import array
def get_array_as_set(array):
        return set(array)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b