import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_perpetuity(payment, rate):
        return payment / rate