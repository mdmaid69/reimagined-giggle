import array
def iterate_over_array(array):
        for item in array:
        print(item)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))