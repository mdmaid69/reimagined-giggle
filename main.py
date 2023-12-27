import array
def convert_array_to_string(array):
        return array.tostring()
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))