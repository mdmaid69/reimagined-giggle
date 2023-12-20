import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time