import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time