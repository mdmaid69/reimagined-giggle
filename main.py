import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5