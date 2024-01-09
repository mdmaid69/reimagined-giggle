import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time