def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()