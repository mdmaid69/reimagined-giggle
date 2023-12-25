import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_perimeter_triangle(a, b, c):
        return a + b + c