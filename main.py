import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time