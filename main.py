import array
def convert_array_to_list(array):
        return array.tolist()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)