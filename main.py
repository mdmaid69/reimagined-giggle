import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_roi(gain, cost):
        return (gain - cost) / cost