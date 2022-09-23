tax = 1.06
delivery_fee = 5

topping = int(input("1 for Plain - $11.50 \n"
                    "2 for Veggie - $12.50 \n"
                    "3 for Pepperoni - $13.50\n"))

if topping == 1:
    pizza_price = 11.50
    description = "Plain"
elif topping == 2:
    pizza_price = 12.50
    description = "Veggie"
elif topping == 3:
    pizza_price = 13.50
    description = "Pepperoni"

delivery = int(input("1 for Delivery - $5.00 \n"
                     "2 for Pickup - Free \n"))

if delivery == 1:
    address = input("Please enter your address for delivery: \n")
elif delivery == 2:
    pass

tip = float(input("Please enter tip amount: $"))

if delivery == 1:
    total = pizza_price * tax + delivery_fee + tip
    print(f"Your total is ${total:.2f}. Pizza will be delivered to {address}.")
elif delivery == 2:
    total = pizza_price * tax + tip
    print(f"Your total is ${total:.2f}.")

