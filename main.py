import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity