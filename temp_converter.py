# Project 04 – Temperature Converter Tool (Starter)

# STEP 1:
# One function is already provided as a placeholder.
# Study this carefully — it shows the correct syntax.

def fahrenheit_to_celsius(fahrenheit):
    # Example placeholder — replace 'pass' with the formula in Step 2C
    pass

# STEP 1 continued:
# Add your own function stubs here:
# 1. celsius_to_fahrenheit
# 2. celsius_to_kelvin

# Example of what a function stub looks like:
# def celsius_to_fahrenheit(celsius):
#     pass


def run_cli():
    print("Temperature Converter")
    print("Convert Celsius to Fahrenheit and Kelvin.")
    print("Type 'q' to quit.\n")

    while True:
        # STEP 3:
        celsius_input = input("Enter temperature in Celsius (or 'q' to quit): ").strip()
        if celsius_input.lower() == "q":
            print("Goodbye!")
            break

        # STEP 3 continued:
        # Convert input to float and call your functions here.
        # Example: f_value = celsius_to_fahrenheit(celsius_value)

        print("(Conversion logic not implemented yet — complete Steps 2–4.)\n")

        # STEP 4:
        # When ready, polish your print output with f-strings.

if __name__ == "__main__":
    run_cli()
