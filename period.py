#calculate period of orbit 

import numpy as np

def calc_period(semi_major_axis, mass):
    return(np.sqrt((4*np.pi**2)/(6.67*10**-11*mass)*semi_major_axis**3))

def main():
    # User inputs
    semi_major_axis_au = float(input("Enter the semi-major axis of the orbit (in AU): "))
    semi_major_axis = semi_major_axis_au*1.496*10**11
    mass_sun = 1.989*10**30
    mass_solar = float(input("Enter the mass of the star (in solar masses): "))
    mass = mass_solar*mass_sun

    print("The period of the orbit is (in seconds):", calc_period(semi_major_axis, mass))
    print("The period of the orbit is (in days):", calc_period(semi_major_axis, mass)/(60*60*24))

if __name__ == "__main__":
    main()