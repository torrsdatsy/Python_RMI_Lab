import Pyro5.server

@Pyro5.server.expose
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity > self.stock:
            excess = quantity - self.stock
            print(f"[SERVER LOG]: Exceeded stocks by {excess} units for {self.name}")
            return f"[ERROR]: Cannot purchase exceeded {quantity}x {self.name}, Only {self.stock} stocks left"
        else:
            self.stock -= quantity
            total = quantity * self.price
            return f"Purchased {quantity}x {self.name} (Total P{total:,.2f})"
            
        

