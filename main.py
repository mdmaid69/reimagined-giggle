import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_circumference_circle(r):
        return 2 * 3.14 * r