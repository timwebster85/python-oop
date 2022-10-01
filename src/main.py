import csv


class Item:

    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, qty=0):
        # Run validations to recieved args
        assert price >= 0, f"Price {price}is not greater than or equal to zero."
        assert qty >= 0, f"Quantity {qty} is not greater than or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.qty = qty

        # Actions to execute
        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.qty

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def load_from_csv(cls):
        with open("src/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                qty = int(item.get('qty')),
            )

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.qty}')"


class Phone(Item):
    pass

phone1 = Phone("iPhone10", 500, 5)
phone1.broken_phone = 1

phone2 = Phone("iPhone13", 800, 10)
phone2.broken_phone = 10



