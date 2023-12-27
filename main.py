def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a