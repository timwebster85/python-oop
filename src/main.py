class Item:
    def __init__(self, name: str, price: float, qty=0):
        # Run validations to recieved args
        assert price >= 0, f"Price {price}is not greater than or equal to zero."
        assert qty >= 0, f"Quantity {qty} is not greater than or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.qty = qty


    def calc_total_price(self):
        return self.price * self.qty


item1 = Item('Phone', 100, 5)

item2 = Item('Laptop', 1300, 80)


print(item1.calc_total_price())
print(item2.calc_total_price())