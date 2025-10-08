def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    print("🌡 Temperature Converter")
    print("Choose the input temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    scale = input("Enter the number of your choice (1/2/3): ")
    try:
        temp = float(input("Enter the temperature value: "))
        
        if scale == "1":
            print(f"🔄 {temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
            print(f"🔄 {temp}°C is {celsius_to_kelvin(temp):.2f}K")
        elif scale == "2":
            print(f"🔄 {temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
            print(f"🔄 {temp}°F is {fahrenheit_to_kelvin(temp):.2f}K")
        elif scale == "3":
            print(f"🔄 {temp}K is {kelvin_to_celsius(temp):.2f}°C")
            print(f"🔄 {temp}K is {kelvin_to_fahrenheit(temp):.2f}°F")
        else:
            print("❌ Invalid scale selection.")
    except ValueError:
        print("❌ Invalid temperature input. Please enter a numeric value.")

if __name__ == "__main__":
    temperature_converter()
