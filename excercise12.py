
quantity = int(input("How many pizzas do you want to order? "))

def get_pizza_order(quantity):
    for i in range (1, quantity + 1):
        toppings = int(input("How many toppings do you want on pizza {}? ".format(i)))
        print("You have ordered a pizza with {} toppings.".format(toppings))
    return

get_pizza_order(quantity)
