import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity