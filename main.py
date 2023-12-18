import array
def extend_array(array, iterable):
        array.extend(iterable)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))