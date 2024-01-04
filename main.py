import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_perpetuity(payment, rate):
        return payment / rate