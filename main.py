def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()