def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a