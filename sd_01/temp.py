def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(temp, original_unit):
    if original_unit.lower() == 'c':
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit.lower() == 'f':
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit.lower() == 'k':
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid input unit. Please use 'C', 'F', or 'K'.")
        return
    
    print(f"{temp} {original_unit.upper()} is equal to:")
    print(f"{fahrenheit:.2f} F")
    print(f"{celsius:.2f} C")
    print(f"{kelvin:.2f} K")

def main():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit of measurement (C/F/K): ")
    convert_temperature(temp, unit)

if __name__ == "__main__":
    main()
