import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time