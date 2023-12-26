def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def get_array_buffer_info(array):
        return array.buffer_info()