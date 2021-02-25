# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)

#Getting the date and time
import datetime
current_time = datetime.datetime.now()
Readable_time = current_time.strftime("%m/%d/%Y %I:%M %p")

#ask the user for a product identifier
selectedIds = []
while True:
    selected_id = input("Please input a product identifier (1-20 are valid, and input DONE when you are finished)")
    if selected_id.upper() == "DONE":
        break
    elif selected_id.upper() != 'DONE' and selected_id.isnumeric() == False:
        print('Sorry, only DONE and the numbers 1-20 are valid inputs. Please try again')
    elif int(selected_id) > products[-1]['id'] or int(selected_id) < products[0]['id']:
        print('Sorry that number is out of the range of 1-20, please try again or enter DONE to finish')
    else:
        selectedIds.append(selected_id)

#start of the receipt
print("-----------------------------------------------")
print("              Stop & Shop")
print("       Visit us at stopandshop.com")
print("-----------------------------------------------")

#printing the time on the receipt
print("    CHECKOUT AT: " + (Readable_time))
print("-----------------------------------------------")
print('Selected Products: ')

#look up information about the product with the given identifier
SubTotal = 0
TaxAmount = 0
TotalPrice = 0
for selected_id in selectedIds:
    matching_products = [x for x in products if x['id'] == int(selected_id)]
    matching_products = matching_products[0]
    SubTotal = (SubTotal + matching_products['price'])
    print('----', matching_products['name'], '(', (str(to_usd(matching_products['price']))), ')')
    TaxAmount = (SubTotal * .0875)
    TotalPrice = (SubTotal + TaxAmount)

#print the End of the Receipt
print("-----------------------------------------------")
print('SUBTOTAL:', str(to_usd(SubTotal)))
print("TAX:", str(to_usd(TaxAmount)))
print("TOTAL:", str(to_usd(TotalPrice)))
print("-----------------------------------------------")
print("       Thank You, See You Again Soon!")
print("-----------------------------------------------")
