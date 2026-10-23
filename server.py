import Pyro5.server
from product import Product

HOST = "127.0.0.1"
PORT = 8000

def RMI_start():
    dm =  Pyro5.server.Daemon(host=HOST, port=PORT)

    laptop = Product(name = "Laptop", price = 55000.00, stock = 10)
    mobile = Product(name = "Android", price = 9000.000, stock = 100)

    dm.register(laptop, objectId = "lab.product")
    dm.register(mobile, objectId = "lab.mobile")

    print(f"Server is running on port {PORT}")
    dm.requestLoop()

if __name__ == "__main__":
    RMI_start()