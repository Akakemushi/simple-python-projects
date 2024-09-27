def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = number * 3 + 1
        print(number)
        return number

num = input("Enter any number: ")
try:
    num = int(num)
    while num != 1:
        num = collatz(num)
except ValueError:
    print("You must enter a number.")