
# DAY NAME  OF THE GIVEN DATE CALCULATOR ALSO TELLS THAT THE GIVEN YEAR IS LEAP YEAR OR NOT 


def day_of_week_calculator(day, month, year):
    if month <= 3:
        month += 12
        year -= 1

    k = year % 100
    c = year // 100
    
    # USING "Zeller's Congruence Formula"

    day_of_the_week = (day + (13 * (month + 1) // 5) + k + (k // 4) + (c // 4) - 2 * c) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    return days[day_of_the_week]


# Function to check given year is leap year or not

def isleap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


# validating the given date 

def validate_date(day, month, year):
    if not (1 <= month <= 12):
        return False, "Invalid month. Please enter a correct month number."

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isleap_year(year):
        days_in_month[2] = 29

    if not (1 <= day <= days_in_month[month]):
        return False, "Invalid day of the month. Please enter a valid day."

    return True, None

 
# taking input from user 

date = input("Enter Date in given format (DD-MM-YYYY):")

try:
    day, month, year = map(int, date.split("-"))
     

    # error message of not valid date 

    is_valid, error_message = validate_date(day, month, year)
    if not is_valid:
        print(error_message)
    
    else:

        # message for leap year
        leap_year_message = "This year is a leap year." if isleap_year(year) else "This year is not a leap year."

        # Calculate the day of the week
        day_of_week = day_of_week_calculator(day, month, year)
        

        # showing final result

        print(f"The day of the week for {date} is {day_of_week}.")
        print(leap_year_message)

except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY.")

