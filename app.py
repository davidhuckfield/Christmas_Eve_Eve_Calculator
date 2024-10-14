from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        # Get the date input from the form
        input_date_str = request.form.get('input_date')
        input_name = request.form.get('input_name')
        input_date = datetime.strptime(input_date_str, '%Y-%m-%d').date()
        message = xmas_eve_calc(input_date, input_name)
    return render_template('index.html', message=message)

def xmas_eve_calc(input_date, input_name):
    xmas_day = date(2024, 12, 25)
    return_string = ""
    input_or_today = ""
    if input_date:
        days = xmas_day - input_date
        input_or_today = input_date.strftime('%m/%d/%y')
    else:
        days = xmas_day - date.today()
        input_or_today = "Today"

    if input_name:
        if (input_name.lower()=="vici"):
            return_string += f"Vici isn't a proper name - did you mean to put Vicky? {input_or_today} is Christmas "
        else:
            return_string = f"Hello {input_name}! {input_or_today} is Christmas "
    else:
        return_string = f"{input_or_today} is Christmas "

    days_number = days.days
    
    for i in range(days_number):
        return_string += "Eve "
    
    return_string += ". There are "
    return_string += str(days_number)
    return_string += " days until Christmas!"
    
    return return_string

if __name__ == '__main__':
    app.run(debug=True)
