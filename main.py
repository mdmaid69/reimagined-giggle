import array
def get_array_as_complex(array):
        return complex(array[0])
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b