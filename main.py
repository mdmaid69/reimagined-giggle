import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))