# Solution Code - Temperature Converter Tool 

<details>
<summary> Step 1 Solution - Define Your Functions</summary>
Python – `temp_converter.py`

```python
# Add these below the fahrenheit_to_celsius stub:
def celsius_to_fahrenheit(celsius):
    pass

def celsius_to_kelvin(celsius):
    pass
``` 
</details>


<details>
<summary>Step 2A Solution – Add Conversion Logic: Celsius to Fahrenheit</summary>
Python – `temp_converter.py`

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    pass
```

</details>  


<details>
<summary>Step 2B Solution – Add Conversion Logic: Celsius to Kelvin</summary>
Python – `temp_converter.py`

```python
def celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
	return celsius + 273.15
```

</details> 


<details>
<summary>Step 2C Solution – Add Conversion Logic: Fahrenheit to Celsius + Quick Test</summary>
Python – `temp_converter.py`

```python
def fahrenheit_to_celsius(fahrenheit):
	celsius = (fahrenheit - 32) * 5/9
	return celsius
    
# ... other functions
```

</details> 


<details>
<summary>Step 3 Solution – Handle User Input</summary>
Python – `temp_converter.py`

```python
celsius_input = input("Enter temperature in Celsius (or 'q' to quit): ").strip()
if celsius_input.lower() == "q":
    print("Goodbye!")
    break

celsius_value = float(celsius_input)
f_value = celsius_to_fahrenheit(celsius_value)
k_value = celsius_to_kelvin(celsius_value)
```
</details>   


<details>
<summary> Step 4 Solution – Format the Output</summary>
Python – `temp_converter.py`

```python
celsius_input = input("Enter temperature in Celsius (or 'q' to quit): ").strip()
if celsius_input.lower() == "q":
    print("Goodbye!")
    break

# Step 3 code here

print(f"{celsius_value:.1f}°C is {f_value:.1f}°F")
print(f"{celsius_value:.1f}°C is {k_value:.1f}K\n")

```
</details>   


<details>
<summary>Final Solution</summary>
Python – `temp_converter.py`

```python
# Project 04 – Temperature Converter Tool (Solution)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def run_cli():
    print("Temperature Converter")
    print("Convert Celsius to Fahrenheit and Kelvin.")
    print("Type 'q' to quit.\n")

    while True:
        celsius_input = input("Enter temperature in Celsius (or 'q' to quit): ").strip()
        if celsius_input.lower() == "q":
            print("Goodbye!")
            break

        celsius_value = float(celsius_input)
        f_value = celsius_to_fahrenheit(celsius_value)
        k_value = celsius_to_kelvin(celsius_value)

        print(f"{celsius_value:.1f}°C is {f_value:.1f}°F")
        print(f"{celsius_value:.1f}°C is {k_value:.1f}K\n")

if __name__ == "__main__":
    run_cli()

```
</details>