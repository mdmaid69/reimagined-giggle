def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)