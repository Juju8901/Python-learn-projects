celsius = input("Please enter degrees in celcius: ")
celsius = float(celsius)

def f_conversion(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print("Your temp in fahrenheit is: " + str(f_conversion(celsius)))