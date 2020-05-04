def make_pizza(size, *toppings):
    print("\nMaking a {} size, -inch pizza with the following toppings: ".format(str(size)))
    for topping in toppings:
        print("- " + topping)
