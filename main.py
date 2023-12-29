import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_perpetuity(payment, rate):
        return payment / rate