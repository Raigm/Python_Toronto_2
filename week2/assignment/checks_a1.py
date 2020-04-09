import a1

print(a1.num_buses(0))
print(a1.num_buses(49))
print(a1.num_buses(50))
print(a1.num_buses(51))

print(a1.stock_price_summary([]))
print(a1.stock_price_summary([0, 0]))
print(a1.stock_price_summary([ -0.02, -0.14, -0.10]))
print(a1.stock_price_summary([0.02, 0.14, 0.10]))
print(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]))

L = [1,2,3,4,5,6]
k = 0
print(a1.swap_k(L, k))


L = [1,2,3,4,5,6]
k = 1
print(a1.swap_k(L, k))


L = [1,2,3,4,5,6]
k = int(len(L)/2)
print(a1.swap_k(L, k))


L = [1,2,3,4,5]
k = int(len(L)/2)
print(a1.swap_k(L, k))

L = ["uno", "dos", "tres", "cuatro"]
k = int(len(L) / 2)

print(a1.swap_k(L, k))

k = int(len(L) / 2)



