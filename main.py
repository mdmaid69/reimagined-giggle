def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)