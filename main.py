import array
def convert_array_to_string(array):
        return array.tostring()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b