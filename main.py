def calculate_work(force, distance):
        return force * distance
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a