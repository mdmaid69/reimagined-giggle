def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))