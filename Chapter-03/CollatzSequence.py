def collatz(number):
    if number%2==0:
        return number//2
    else:
        return ((3*number)+1)
try:
    n=int(input("Enter a number:"))
    collatz(n)
except ValueError:
    n=int(input("Enter a valid number:"))

while n != 1:
    n=collatz(n)
    print(n)