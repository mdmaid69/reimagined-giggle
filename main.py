from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_energy(mass, c=3*10**8):
        return mass * c**2