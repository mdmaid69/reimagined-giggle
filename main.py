import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time