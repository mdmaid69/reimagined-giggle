def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)