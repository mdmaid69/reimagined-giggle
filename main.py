def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()