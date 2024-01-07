def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)