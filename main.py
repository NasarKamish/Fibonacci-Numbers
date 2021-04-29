def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


word = ""
for i in range(0, (int(input("Enter your number: ")))):
    word = word + " " + str(fib(i))

print("Your Fibonacci patten is: ")
print(word)
