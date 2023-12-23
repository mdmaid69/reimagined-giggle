import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)