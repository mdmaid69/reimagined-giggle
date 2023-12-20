import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)