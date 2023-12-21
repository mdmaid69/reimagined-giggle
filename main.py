import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities