import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue