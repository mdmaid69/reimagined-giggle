import array
def get_array_item(array, i):
        return array[i]
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)