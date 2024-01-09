def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)