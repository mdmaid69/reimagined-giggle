import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread