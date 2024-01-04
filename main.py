import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue