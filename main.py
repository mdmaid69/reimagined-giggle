import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)