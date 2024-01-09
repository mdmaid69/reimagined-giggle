def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}