from flask import Flask, render_template, request

app = Flask(__name__)

def isleap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_date(day, month, year):
    if not (1 <= month <= 12):
        return False, "Invalid month. Please enter a correct month number."

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isleap_year(year):
        days_in_month[2] = 29

    if not (1 <= day <= days_in_month[month]):
        return False, "Invalid day of the month. Please enter a valid day."

    return True, None

def day_of_week_calculator(day, month, year):
    if month <= 3:
        month += 12
        year -= 1

    k = year % 100
    c = year // 100

    day_of_the_week = (day + (13 * (month + 1) // 5) + k + (k // 4) + (c // 4) - 2 * c) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    return days[day_of_the_week]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_input = request.form['date']
        day, month, year = map(int, date_input.split('-')[::-1])  # Split and reverse to get day, month, year
        
        is_valid, error_message = validate_date(day, month, year)
        if not is_valid:
            return render_template('index.html', error=error_message)
        
        day_of_week = day_of_week_calculator(day, month, year)
        is_leap = isleap_year(year)
        leap_year_message = "The year is a leap year." if is_leap else "The year is not a leap year."
        
        return render_template('index.html', day_of_week=day_of_week, leap_year_message=leap_year_message, date=date_input)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
