sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))