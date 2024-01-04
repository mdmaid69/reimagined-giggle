def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()