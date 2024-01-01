import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def calculate_irr(cash_flows):
        rate = 0.1
        for _ in range(100):
        npv = sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
        if abs(npv) < 1e-6:
                return rate
        rate += 0.01
        return None