# #calculate absolute magnitude given distance and apparent magnitude

import numpy as np

def calc_abs_mag(app_mag, distance_pc):
    return(app_mag - 5*np.log10(distance_pc) + 5)

def main():
    # User inputs
    app_mag = float(input("Enter the apparent magnitude of the object: "))
    distance_pc = float(input("Enter the distance to the object (in parsecs): "))

    print("The absolute magnitude of the object is:", calc_abs_mag(app_mag, distance_pc))

if __name__ == "__main__":
    main()