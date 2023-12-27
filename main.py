import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_speed(distance, time):
        return distance / time