def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a