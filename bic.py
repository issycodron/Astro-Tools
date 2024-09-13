import numpy as np

def calculate_BIC(chi_squared, free_params, sample_size):
    return chi_squared + free_params * np.log(sample_size)

def main():
    # User inputs
    DoF = int(input("Enter the degrees of freedom (DoF): "))
    chi_squared = float(input("Enter the chi-squared value: "))
    free_params = int(input("Enter the number of free parameters: "))
    sample_size = DoF + free_params
    #sample_size = int(input("Enter the sample size (n): "))

    # Calculate BIC
    BIC = calculate_BIC(chi_squared * DoF, free_params, sample_size)

    # Print the result
    print("Bayesian Information Criterion (BIC):", BIC)

if __name__ == "__main__":
    main()
