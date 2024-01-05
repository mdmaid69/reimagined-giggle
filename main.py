import array
def iterate_over_array(array):
        for item in array:
        print(item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)