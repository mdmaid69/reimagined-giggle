import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_average(numbers):
        return sum(numbers) / len(numbers)