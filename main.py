import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time