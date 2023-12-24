def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()