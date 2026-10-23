import Pyro5.api

#initialize proxy, connect to the remote objects
laptop_prox = Pyro5.api.Proxy("PYRO:lab.product@127.0.0.1:8000")
mobile_prox = Pyro5.api.Proxy("PYRO:lab.mobile@127.0.0.1:8000")
bag_prox = Pyro5.api.Proxy("PYRO:lab.bag@127.0.0.1:8000")
chr_prox  = Pyro5.api.Proxy("PYRO:lab.charger@127.0.0.1:8000")

#Client pruchasing items
print("[Client]: Ordered items:")
print(laptop_prox.purchase(9))
print(mobile_prox.purchase(10))
print(bag_prox.purchase(15))
print(chr_prox.purchase(5))

#Invoke methods
laptop_prox._pyroRelease
mobile_prox._pyroRelease
bag_prox._pyroRelease
chr_prox._pyroRelease



