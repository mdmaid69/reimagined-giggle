import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding