def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a