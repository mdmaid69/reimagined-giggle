def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def convert_array_to_bytes(array):
        return array.tobytes()