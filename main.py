import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets