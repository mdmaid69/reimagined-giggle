def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import shutil
def delete_directory(path):
        shutil.rmtree(path)