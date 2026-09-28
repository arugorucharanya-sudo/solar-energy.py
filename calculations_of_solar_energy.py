calculations_of_solar_energy.py

print("SOLAR ENERGY CALCULATOR")
print("-----------------------")

voltage = float(input("Enter solar panel voltage (V): "))
current = float(input("Enter solar panel current (A): "))
sun_hours = float(input("Enter sunlight hours per day: "))
efficiency = float(input("Enter system efficiency (%): "))

 Solar panel power
power = voltage * current

Convert efficiency to decimal
efficiency_decimal = efficiency / 100

Daily energy
daily_energy = power * sun_hours * efficiency_decimal

print("\n--- Solar Energy Results ---")
print("Panel Power =", round(power, 2), "W")
print("Daily Energy =", round(daily_energy, 2), "Wh")
print("Daily Energy =", round(daily_energy / 1000, 2), "kWh")
