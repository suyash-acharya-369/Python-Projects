# Conversion of temperature between Fahrenheit and Celcius Using conditional statements:

Temperature = float(input("Enter the temperature value: "))
Unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ").upper()

if Unit == 'C':
    Result = ((9/5)*Temperature) + 32
    print(f'Temperature in Fahrenheit is {Result}°F')

elif Unit == 'F':
    Result = (5/9)*(Temperature - 32)
    print(f'Temperature in Celsius is {Result}°C')  

else:
    print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Example Inputs and Outputs:
# Input: 100 C  
# Output: Temperature in Fahrenheit is 212.0°F
# Input: 32 F
# Output: Temperature in Celsius is 0.0°C



