item1 = "Phone"
item1_price = 100
item1_qty = 5
item_total_price = item1_price * item1_qty


class Item_details:
    def __init__(self, price, qty, item):
        self.item = item
        self.qty = qty
        self.price = price
        self.x = x

    def item_total_price(self):
        total_price = self.price * self.qty

        return total_price

    def item_desc(self):
        if self.item == "Phone":
            desc = "This is a balck iPhone"
        else:
            desc = "This is not an iPhone"

        return desc, self.x


cat = Item_details(100, 5, "Phone1")
print(cat.item_desc())
print(cat.item_total_price())
