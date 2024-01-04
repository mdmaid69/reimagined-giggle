import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity