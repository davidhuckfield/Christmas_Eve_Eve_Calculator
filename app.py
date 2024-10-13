from flask import Flask, render_template
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def home():
    message = xmas_eve_calc()
    return render_template('index.html', message=message)

def xmas_eve_calc():
    input_date = date(2024, 10, 13)
    xmas_day = date(2024, 12, 25)
    days = xmas_day - input_date
    print(days)
    return_string="Today is Christmas "
    days_number = days.days
    for i in range(days_number):
        return_string += "Eve "
  
    return_string += ". There are "
    return_string += str(days_number)
    return_string += " days until Christmas!"
    print(return_string)
    return return_string

if __name__ == '__main__':
    app.run(debug=True)