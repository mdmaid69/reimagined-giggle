import array
def get_array_as_complex(array):
        return complex(array[0])
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))