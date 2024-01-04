import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time