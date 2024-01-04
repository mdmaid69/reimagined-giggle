import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")