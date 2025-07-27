FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsuis):
    return (celsuis * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to convert: "))
cel_or_fah = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if cel_or_fah == "C" and temp != None:
    fah = convert_to_fahrenheit(temp)
    print(f"{temp} degress celsius is {fah} degress fahrenheit.")
elif cel_or_fah == "F" and temp != None:
    cel = convert_to_celsius(temp)
    print(f"{temp} degress fahrenheit is {cel} degress celsius.")
else:
    print("Please provide the necessary inputs for both temperature and unit.")