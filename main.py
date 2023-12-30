import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)