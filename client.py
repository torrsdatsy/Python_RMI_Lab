import Pyro5.api

laptop_prox = Pyro5.api.Proxy("PYRO:lab.product@127.0.0.1:8000")
mobile_prox = Pyro5.api.Proxy("PYRO:lab.mobile@127.0.0.1:8000")

print("[Client]: Ordering...")
print(laptop_prox.purchase(9))

print("\n[Client]: Ordering...")
print(mobile_prox.purchase(10))

laptop_prox._pyroRelease
mobile_prox._pyroRelease



