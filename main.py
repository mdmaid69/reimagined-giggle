import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time