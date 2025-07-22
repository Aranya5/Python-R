# This program converts temperature from Celsius to Fahrenheit
cel = float(input("Enter temperature in Celsius: "))
fahr = (9.0 * cel) / 5.0 + 32.0
print("Temperature in Fahrenheit:", fahr)

# This program converts temperature from Fahrenheit to Celsius
fahr = float(input("Enter temperature in Fahrenheit: "))
cel = (fahr - 32.0) * 5.0 / 9.0
print("Temperature in Celsius:", cel)