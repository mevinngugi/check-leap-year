"""
A function that checks whether a year is leap year or not
"""

# A try block to ensure the user input is not a string
try:

    def check_leap_year(user_input):
        if isinstance(user_input, int):  # Checks if user input is of type int
            if user_input < 525:  # Start of the AD calendar
                return "Please enter a year greater or equal to the year 525.\nFun fact: The AD calendar started in the year 525."
            elif (
                user_input % 100 == 00
            ):  # The century year is a leap year only if it is perfectly divisible by 400
                if isinstance(user_input / 400, int):
                    return f"{user_input} a leap year"
                else:
                    return f"{user_input} not a leap year"
            else:
                if user_input % 4 == 0:
                    return f"{user_input} a leap year"
                else:
                    return f"{user_input} not a leap year"


except:
    print("Sorry... Please key in year in numbers. eg: 1987")

user_input = int(input("Which year do you want to check if it's a leap year or not? "))

print(check_leap_year(user_input))
