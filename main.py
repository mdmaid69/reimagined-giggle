def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()