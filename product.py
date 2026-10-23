import Pyro5.server

@Pyro5.server.expose
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            total = quantity * self.price
            return f"Purchased {quantity}x {self.name} (Total P{total:,.2f})"
        return f"Only {self.stock} stocks left"

