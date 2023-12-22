def calculate_speed(distance, time):
        return distance / time
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a