import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)