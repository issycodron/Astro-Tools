import numpy as np


def masToAU(distance, mas):
    return distance * mas*1e-3

def main():
    # User inputs
    distance = float(input("Enter the distance to the object (in parsecs): "))
    mas = float(input("Enter the angular size of the object (in milliarcseconds): "))

    # Calculate the size of the object in AU
    size_AU = masToAU(distance, mas)

    # Print the result
    print("The size of the object in AU is:", size_AU)

if __name__ == "__main__":
    main()





