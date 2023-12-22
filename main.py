import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps