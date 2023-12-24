def calculate_perpetuity(payment, rate):
        return payment / rate
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a