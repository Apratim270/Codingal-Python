def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh Lemonades only for you.")
greet_customer()
price_per_cup=float(input("Enter the Price of per cup in dollars :"))
cups_sold=int(input("Enter the number of cups sold:"))
def calculate_total(price,cups):
    total=price*cups
    return total
total_cost=calculate_total(price_per_cup,cups_sold)
rounded_total=round(total_cost,2)
print("Total Cost",rounded_total)
amount_paid=float(input("Enter the amount paid by the customer:"))
def calculate_change(paid,total):
    change=paid-total
    return change
change_due=calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)
def thank_you_message(cups_sold):
    if cups_sold>=5:
        return ";Wow!big order, Thanks for your support"
    else:
        return "Thanks for stopping by the stand!"
closing_message=thank_you_message(cups_sold)
print("Cost per cup",price_per_cup)
print("Cups Sold",cups_sold)
print("Total Cost ",rounded_total)
print("Amount paid",amount_paid)
print("Change due,",rounded_change)
print(closing_message)