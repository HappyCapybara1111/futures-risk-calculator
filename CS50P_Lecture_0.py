def main():
    print("Hello World")
    hello()

# Ask user for their name and remove white space from str and capitalize user's name
name = input("Enter your name: ").strip().title()

# formatted string, 大括號 {} 內可以放 variable 或 expression
print(f"hello {name}")

#int means integers
#float means decimals

x = float(input("What's your favorite number? "))
y = float(input("Lets enter another number: "))
z = round(x + y, 2)
print(f"Your favorite number is {z}")

#def means define
def hello(to):
    print("hello,", to)

    main()
