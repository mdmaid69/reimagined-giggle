  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"