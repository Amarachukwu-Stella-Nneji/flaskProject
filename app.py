from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/convert/<float:celsius>')
def convert_celsius_route(celsius):
    return convert_celcius_to_fahrenheit(celsius)


@app.route('/convert/<float:fahrenheit>')
def convert_fahrenheit_route(fahrenheit):
    return convert_fahrenheit_to_celsius(fahrenheit)


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius


def convert_celcius_to_fahrenheit(celcius):
    """Convert celsius to fahrenheit."""
    result = celcius * 9.0 / 5 + 32
    return f"The result is: {result}"


if __name__ == '__main__':
    app.run()
