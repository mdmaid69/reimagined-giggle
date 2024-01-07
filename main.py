import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)