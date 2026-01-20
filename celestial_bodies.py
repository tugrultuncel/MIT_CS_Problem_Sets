"""
Docstring for celestial_bodies
This module calculates how long a year takes on different celestial bodies according to earth years.
"""
from math import sqrt

# Celestial constants
Solar_mass = 1.989e30  # kg
Earth_mass = 5.972e24  # kg
AU = 1.496e11  # meters (Astronomical Unit)

G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
PI = 355/113  # Approximation of pi

def get_numeric_input(prompt):
    """Asks for input until a valid numeric value is provided."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

celestial_body_name = input("Enter the name of the celestial body: ")
m_star = get_numeric_input("Enter the mass of the star (in Solar masses): ") * Solar_mass
m_body = get_numeric_input("Enter the mass of the celestial body (in Earth masses): ") * Earth_mass
r = get_numeric_input("Enter the orbital radius (in AU): ") * AU

# Calculate orbital period using Kepler's third law (result in seconds)
T_seconds = 2 * PI * sqrt((r**3) / (G * (m_star + m_body)))

# Convert seconds to years (1 year = 365.25 days)
seconds_per_year = 60 * 60 * 24 * 365.25
T = T_seconds / seconds_per_year

print("The time taken for one year on", celestial_body_name, "is", T, "Earth years.")