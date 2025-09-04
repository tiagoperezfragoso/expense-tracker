import functions

print("Welcome to the expense tracker system")
option = functions.menu()

match option:
    case 1:
        functions.add_expense(functions.expenses)
    case 2:
        functions.list_expense(functions.expenses)
    case 3:
        functions.search_period(functions.expenses)
    case 4:
        functions.list_expense(functions.expenses)
    case 6:
        functions.search_category(functions.categories)
    case 7:


