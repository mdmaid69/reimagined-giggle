n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)