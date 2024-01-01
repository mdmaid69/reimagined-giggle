def calculate_average(lst):
        return sum(lst) / len(lst)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)