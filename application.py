from flask import Flask, render_template, request
from datetime import datetime, date

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        # Get the date input from the form
        input_date_str = request.form.get('input_date')
        input_name = request.form.get('input_name')

        try:
            input_date = datetime.strptime(input_date_str, '%Y-%m-%d').date() if input_date_str else None
        except ValueError:
            input_date = None
        
        message = xmas_eve_calc(input_date, input_name)

    return render_template('index.html', message=message)

def xmas_eve_calc(input_date, input_name):
    xmas_day = date(date.today().year, 12, 25)
    return_string = ""
    # display variable depending on input or blank
    input_or_today = ""

    #if input date exists / date has been inputted
    if input_date:
        input_year = input_date.year
        xmas_day = date(input_year, 12, 25)
        days = xmas_day - input_date
        input_or_today = input_date.strftime('%m/%d/%y')
    #else set day to today
    else:
        days = xmas_day - date.today()
        input_or_today = "Today"

    if input_name:
        return_string = f"Hello {input_name}! {input_or_today} is Christmas "
    else:
        return_string = f"{input_or_today} is Christmas "
#extract days number from date object
    days_number = days.days

    for i in range(days_number):
        if i < days_number-1:
            return_string += "Eve "
        else:
            return_string += "Eve."
    
    return_string += " There are "
    return_string += str(days_number)
    return_string += " days until Christmas!"
    
    return return_string

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)


