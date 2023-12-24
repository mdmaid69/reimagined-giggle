import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def convert_to_binary(n):
        return bin(n)