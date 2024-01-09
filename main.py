import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue