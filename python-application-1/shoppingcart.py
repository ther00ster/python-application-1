class ShoppingCart:

    def __init__(self, *args, **kwargs):
        # return super().__init__(*args, **kwargs)
        self.items = []

    def addItem(self, name, price):

        item = (name, price)
        self.items.append(item)

    def __iter__(self):

        return self.items.__iter__()

    # @property is essentially the getter -- used here on the TotalPrice property of a ShoppingCart
    @property
    # a member property looks like a function that takes "self" as the only parameter
    def TotalPrice(self):
        """The sum of all items in the ShoppingCart"""

        total = 0
        for item in self.items:
            total += item[1]

        return total

cart = ShoppingCart()
cart.addItem('car', 20000)
cart.addItem('tv', 500)

for item in cart:
    print(item)
    
print("Total price is ${0} (or...${0:,})".format(cart.TotalPrice))
