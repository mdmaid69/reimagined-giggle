import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)