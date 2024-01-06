def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import shutil
def delete_directory(path):
        shutil.rmtree(path)