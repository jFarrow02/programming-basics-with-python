calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days = 0): # You can supply default values for params in Python
    condition_check = num_of_days >= 0
    print(type(condition_check))
    # Return output if number of days is positive
    if(condition_check):
        return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    else:
        return("Invalid input provided. You must provide a positive integer for number of days.")


x = int(input("Input a number of days for conversion to hours:\n"))

print(days_to_units(x))
    