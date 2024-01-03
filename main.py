import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))