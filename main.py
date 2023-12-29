import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)