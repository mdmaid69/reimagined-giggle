import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding