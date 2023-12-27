def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import array
def remove_from_array(array, item):
        array.remove(item)