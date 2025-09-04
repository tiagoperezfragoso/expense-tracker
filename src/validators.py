from datetime import datetime

def validate_date(date):
    try:
        valid_date = datetime.strptime(date,"%d-%m-%Y")
        return valid_date.date()
    except ValueError:
        print(f"Invalid date format. Please use dd-mm-yyyy.")
        return False
def validate_type(type):
    valid_type = ["expense", "income"]
    if type.lower() in valid_type:
        return True
    else:
        print("The type is incorret, please insert only one of the accepted types: expense or income!")
        return False

