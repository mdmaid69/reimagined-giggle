def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()