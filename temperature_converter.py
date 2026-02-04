print("Temperature Conversion Program")
print("Convert between Celsius, Fahrenheit, and Kelvin")

temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C / F / K): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"{temperature} °C = {fahrenheit:.2f} °F")
    print(f"{temperature} °C = {kelvin:.2f} K")

elif unit == "F":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temperature} °F = {celsius:.2f} °C")
    print(f"{temperature} °F = {kelvin:.2f} K")

elif unit == "K":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temperature} K = {celsius:.2f} °C")
    print(f"{temperature} K = {fahrenheit:.2f} °F")

else:
    print("Invalid unit entered. Please use C, F, or K.")

