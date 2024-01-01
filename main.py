import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def find_unique_words(sentence):
        return set(sentence.split())