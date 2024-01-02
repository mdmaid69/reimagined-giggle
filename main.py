import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_volume(length, width, height):
        return length * width * height