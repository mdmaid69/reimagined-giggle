import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()