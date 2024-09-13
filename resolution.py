#### calculate telescope resolution ####

import numpy

def calc_resolution(wavelength, baseline_length):
    return(wavelength/(2*baseline_length))
#input wavelength as microns so convert to meters by multiplying by 10^-6

def main():
    # User inputs
    wavelength = float(input("Enter the wavelength of the light (in microns): "))*10**-6
    baseline_length = float(input("Enter the baseline length (in meters): "))

    # Calculate the resolution
    resolution = calc_resolution(wavelength, baseline_length)

    # Print the result
    print("The resolution is:", resolution)

# convert resolution from radians into arcseconds
    resolution = resolution*((3600*180)/numpy.pi)
    print("The resolution is:", resolution, "arcseconds")

# convert arcseconds to milliarcseconds
    resolution = resolution*1000
    print("The resolution is:", resolution, "milliarcseconds")

if __name__ == "__main__":
    main()

