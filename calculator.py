print("Welcome to a basic calculator app")
first = float(input("First Number: "))
second = float(input("Second Number: "))

choice = input("Type operation (Plus, Subtract, Multiply, or Divide): ")

if choice.upper() == "PLUS":
    result = first + second
    print("Result: " + str(result))
elif choice.upper() == "SUBTRACT":
    result = first - second
    print("Result: " + str(result))
elif choice.upper() == "MULTIPLY":
    result = first * second
    print("Result: " + str(result))
elif choice.upper() == "DIVIDE":
    if second != 0:
        result = first / second
        print("Result: " + str(result))
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation. Please choose Plus, Subtract, Multiply, or Divide.")


