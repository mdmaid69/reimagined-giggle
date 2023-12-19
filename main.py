def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)