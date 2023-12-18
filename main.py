import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time