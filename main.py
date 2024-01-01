def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a