import os
def change_working_directory(path):
        os.chdir(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost