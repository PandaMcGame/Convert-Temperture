def convert_fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit-32) * 5 / 9
    return "{:.1f} °C".format(celsius)


def convert_celsius_to_fahrenheit(celsius: float):
    fahrenheit = celsius * 9/5 + 32
    return "{:.1f} °F".format(fahrenheit)
