def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a