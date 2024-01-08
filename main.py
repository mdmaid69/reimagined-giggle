n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)