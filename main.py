import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_roi(gain, cost):
        return (gain - cost) / cost