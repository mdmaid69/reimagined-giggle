import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)