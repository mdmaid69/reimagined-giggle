import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time