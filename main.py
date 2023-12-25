def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a