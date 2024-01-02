import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))