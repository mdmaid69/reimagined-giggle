def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()