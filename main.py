import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)