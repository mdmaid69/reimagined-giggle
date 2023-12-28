import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_acceleration(speed, time):
        return speed / time