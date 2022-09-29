from pprint import pprint

class Item:
    pay_rate = 0.8 # pay rate after 20% discount

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

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate



item1 = Item('Phone', 100, 5)
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)