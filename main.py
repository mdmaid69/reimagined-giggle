n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import array
def convert_array_to_bytes(array):
        return array.tobytes()