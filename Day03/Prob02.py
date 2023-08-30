
def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)

niter = int(input("Enter the number of fibanocci series to be generated :"))
print("Fibanocci Series")
for i in range(niter):
    print(fibo(i), end=" ")
print()

