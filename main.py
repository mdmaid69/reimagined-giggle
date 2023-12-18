import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))