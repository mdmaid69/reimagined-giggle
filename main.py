import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_area(radius):
        return 3.14 * radius * radius