  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"