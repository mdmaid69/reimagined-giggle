import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue