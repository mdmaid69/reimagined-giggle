def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()