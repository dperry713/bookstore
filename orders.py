def get_valid_quantity():
    while True:
        try:
            quantity = int(input("How many copies of the novel would you like to order? "))
            if quantity > 0:
                print(f"Great choice! You've ordered {quantity} copies. Enjoy your reading!")
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Oops! That's not a valid quantity. Please enter a positive whole number.")

get_valid_quantity()
