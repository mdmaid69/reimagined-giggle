import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)