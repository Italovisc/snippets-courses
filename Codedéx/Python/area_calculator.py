choice = ""

while choice not in ["1", "2", "3", "4", "5"]:
    if choice not in ["1", "2", "3", "4", "5"]:
        print("\nWrong input! Try again.")

    print("""\n=================
AREA CALCULATOR
=================
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit""")

    choice = input("Choice: ")

# TRIANGLE
if choice == "1":
    height = float(input("\nHeight: "))
    base = float(input("Base: "))

    print(f"\nThe area is {(height * base) / 2}")
# RECTANGLE
elif choice == "2":
    length = float(input("\nLength: "))
    width = float(input("Width: "))

    print(f"\nThe area is {length * width}")
# SQUARE
elif choice == "3":
    side = float(input("\nSide: "))

    print(f"\nThe area is {side * side}")
# CIRCLE
elif choice == "4":
    radius = float(input("\nRadius: "))

    print(f"\nThe area is {3.14 * radius ** 2}")
# QUIT
elif choice == "5":
    print("\nExiting...")
