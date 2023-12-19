import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time