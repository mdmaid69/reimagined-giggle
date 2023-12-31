import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))