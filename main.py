def calculate_volume(length, width, height):
        return length * width * height
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))