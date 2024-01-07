def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()