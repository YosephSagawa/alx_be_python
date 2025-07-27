FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try: 
    temp = float(input("Enter the temperature to convert: "))
except (ValueError, TypeError):
    print("Invalid temperature. Please enter a numeric value.")
    exit()
cel_or_fah = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if cel_or_fah == "C":
    fah = convert_to_fahrenheit(temp)
    print(f"{temp} degrees celsius is {fah} degress fahrenheit.")
elif cel_or_fah == "F":
    cel = convert_to_celsius(temp)
    print(f"{temp} degrees fahrenheit is {cel} degress celsius.")
else:
    print("Please provide the necessary input for unit.")