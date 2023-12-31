import array
def get_list_from_array(array):
        return array.tolist()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)