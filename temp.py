import numpy as np

def calc_sublimation_temp(radius, luminosity,epsilon):
    return(np.sqrt(((1/1500)**(-2)*1.1*np.sqrt(epsilon)*(luminosity/1000)**(0.5))/radius))

def main():
    # User inputs
    radius = float(input("Enter the sublimation radius (in au): "))
    luminosity = float(input("Enter the luminosity of the star (in solar luminosities): "))
    epsilon = float(input("Enter cooling efficiency (=<1): "))

    # Calculate the sublimation temperature
    sublimation_temp = calc_sublimation_temp(radius, luminosity,epsilon)

    # Print the result
    print("The sublimation temperature is:", sublimation_temp)

if __name__ == "__main__":
    main()
    