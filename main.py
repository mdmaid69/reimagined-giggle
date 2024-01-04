import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)