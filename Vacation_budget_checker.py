# Vacation budget checker for a trip

days_of_vacation = float(input("Enter duration of your vacation in days: "))
food_per_day = float(input("Enter the amount of money you will need for food for one day of your vacation: "))
hotel_per_day = float(input("Enter the amount of money you will need for one hotel night: "))
ticket_price = float(input("Enter the price of the ticket to the destination place: "))
return_ticket_price = float(input("Enter the price of return ticket: "))
possible_additional_expenses = float(input("Enter the amount of money for any additional possible expenses: "))

needed_budget = days_of_vacation * food_per_day + days_of_vacation * hotel_per_day + ticket_price \
                + return_ticket_price + possible_additional_expenses
print("You will need " + str(needed_budget) + " dollars. Have a nice trip!")
