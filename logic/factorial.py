fac = int(input("Enter your number :"))
def factorial(fac):
    if fac == 0:
        return 1
    else:
        return fac * factorial(fac-1)
print(factorial(fac))
