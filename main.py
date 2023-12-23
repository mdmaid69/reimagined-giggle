import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)