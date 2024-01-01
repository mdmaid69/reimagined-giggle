import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5