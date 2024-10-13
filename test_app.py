from datetime import datetime, date

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

xmas_eve_calc()