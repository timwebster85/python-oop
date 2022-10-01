from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, qty=0, broken_phones=0):
        # Call to super function
        super().__init__(
            name, price, qty
        )

    # Run validations to recieved args
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero."

        # Assign to self object
        self.broken_phones = broken_phones