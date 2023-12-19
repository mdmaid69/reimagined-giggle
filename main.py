n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)