numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)