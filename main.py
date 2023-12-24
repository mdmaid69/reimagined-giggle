from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True