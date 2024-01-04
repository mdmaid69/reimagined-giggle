import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)