import json
from pathlib import Path
import validators
from datetime import datetime

expenses_file = Path(__file__).resolve().parent.parent / "data/expenses.json"
categories_file = Path(__file__).resolve().parent.parent / "data/categories.json"


def menu():
    print("1-Insert expense/income")
    print("2-Remove expense/income")
    print("3-Report per month")
    print("4-List all expenses")
    print("5-List all incomes")
    print("6-List by category")

    option = int(input("Please, select an option:"))
    return option

def load_expenses():
    if expenses_file.exists():
        if expenses_file.stat().st_size == 0:
            # file exists but is empty
            return []
        with expenses_file.open("r", encoding="utf-8") as f:
            return json.load(f)   # safe to read because file has content
    else:
        return []  # no file yet

expenses = load_expenses()

def load_categories():
    if categories_file.exists():
        if categories_file.stat().st_size == 0:
            # file exists but is empty
            return []
        with categories_file.open("r", encoding="utf-8") as f:
            return json.load(f)   # safe to read because file has content
    else:
        return []  # no file yet

def save_expense(expense):
    with open(expenses_file, "w") as file:
        json.dump(expenses, file, indent=4)

categories = load_categories()

def save_categories(expense):
    with open(categories_file, "w") as file:
        json.dump(categories, file, indent=4)

def list_category(category):

    for item in categories:
        print(f'{categories.index(item)} - {item["category"]}')

    category_option = int(input(f'Insert the option that correspond to the desired category: '))

    if category_option == 0:
        new_category = str(input(f'Insert the new category name:'))
        categories.append({"category":new_category})
        category = new_category
        save_categories(categories)
    else:
        category = categories[category_option]

    return category["category"]


def add_expense(expense):
    new_date = input("Inform the Date for the expense: ")
    while not validators.validate_date(new_date):
        new_date = input("Inform the Date for the expense: ")
    new_description = input("Insert the description for the expense: ")
    new_category = list_category(categories)
    new_value = float(input("What is the expense's value: "))
    new_type = input("What is the type(expense/income): ")
    while not validators.validate_type(new_type):
        new_type = input("What is the type(expense/income): ")

    new_expense = {
        "dateTime": new_date,
        "description": new_description,
        "category": new_category,
        "value": new_value,
        "type": new_type
    }
    expenses.append(new_expense)

    save_expense(expenses)

def list_expense(expenses):
    print('| Date | Description | Category | Value | Type | ')
    for item in expenses:
        print(f'{item["dateTime"]} | {item["description"]} | {item["category"]} | {item["value"]} | {item["type"]} |')
        print("---------------------------------------------")

def get_month(date):
    month = int(datetime.strptime(date, "%d-%m-%Y").month)
    return month

def get_year(date):
    year = int(datetime.strptime(date, "%d-%m-%Y").year)
    return year


def search_period(expenses):
    month = int(input("Insert the month(ex 02):"))
    year = int(input("insert the year(ex 2025)"))

    print(f"Report period(month) from {month} of {year}")
    print('| Date | Description | Category | Value | Type | ')

    for item in expenses:
        if month == get_month(item["dateTime"]) and year == get_year(item["dateTime"]):
            print(f'{item["dateTime"]} | {item["description"]} | {item["category"]} | {item["value"]} | {item["type"]} |')
            print("---------------------------------------------")
        else:
            continue

def search_category(categories):

    category = list_category(categories)
    print(category)

    for item in expenses:
        if item["category"] == category:
            print(f'{item["dateTime"]} | {item["description"]} | {item["category"]} | {item["value"]} | {item["type"]} |')
            print("---------------------------------------------")
        else:
            continue

def get_date(expense):
    """Extract the date from an expense and return it as a datetime object."""
    return datetime.strptime(expense["date"], "%Y-%m-%d")

def list_expenses_by_date(expense):
    """Load, sort, and print the expenses by date."""
    expenses_sorted = sorted(expenses, key=get_date)

    for expense in expenses_sorted:
        print(f"{expense['date']} - {expense['name']}: ${expense['amount']}")


