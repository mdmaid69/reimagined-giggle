import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue