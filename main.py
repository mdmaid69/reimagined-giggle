import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_acceleration(speed, time):
        return speed / time