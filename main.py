def calculate_roi(gain, cost):
        return (gain - cost) / cost
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a