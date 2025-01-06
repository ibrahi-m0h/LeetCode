# You are writing a program to help with temperature conversions. Your program should:

# Display the current temperature in Celsius.
# Allow the user to convert the temperature to Fahrenheit.
# Display the converted temperature in Fahrenheit.
# Use functions to organize your code, such as one function to display the temperature and another function to perform the conversion. For example, if the current temperature is 25°C, the program should calculate and display the equivalent in Fahrenheit.

# Celcius conversion: (0°C × 9/5) + 32

temp_celsius = 30

def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5) + 32)

temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)

print(temp_fahrenheit)