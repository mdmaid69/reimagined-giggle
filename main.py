import array
def get_array_index(array, item):
        return array.index(item)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))