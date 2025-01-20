def check_temperature(temp):
    if temp >= 20:
        return "It's warm enough for light clothes."
    else:
        return "It's too cold for light clothes."

# Example usage
temperature = float(input("Enter the temperature in Celsius: "))
print(check_temperature(temperature))