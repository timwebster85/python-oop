import csv


class Item:

    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, qty=0):
        # Run validations to recieved args
        assert price >= 0, f"Price {price}is not greater than or equal to zero."
        assert qty >= 0, f"Quantity {qty} is not greater than or equal to zero."

        # Assign to self object
        self.__name = name
        self.__price = price
        self.qty = qty

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + (self.__price * increment_value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calc_total_price(self):
        return self.__price * self.qty

    @classmethod
    def load_from_csv(cls):
        with open("src/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                qty=int(item.get("qty")),
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
        return f"{self.__class__.__name__}('{self.name}, {self.__price}, {self.qty}')"

    def __connect(self, smtp_Server):
        x = smtp_Server
        return f"{x} connected to SMTP server."

    def __prepare_body(self):
        return f"""
        Hello,
        The product:{self.name} has a quantity of: {self.qty} units
        
        Regards,
        Warehouse"""

    def __send(self):
        return "Message sending..."

    def send_email(self):
        self.__connect('Test_smtp')
        self.__prepare_body()
        self.__send()
        return "Message sent."
