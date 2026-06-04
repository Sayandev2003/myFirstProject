print("1. Add")
print("2. Substruct")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose an option: "))

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if choice == 1:
    print("Result = ", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result = ", num1 * num2)
elif choice == 4:
    print("Result = ", num1 / num2)
else:
    print("Invalid option")
