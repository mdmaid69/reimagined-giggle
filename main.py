import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal