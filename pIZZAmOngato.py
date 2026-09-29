Pizza = [
    ("Pepperoni", "Small", 100),
    ("Pepperoni", "Medium", 120),
    ("Pepperoni", "Large", 150),

    ("Ham & Cheese", "Small", 100),
    ("Ham & Cheese", "Medium", 120),
    ("Ham & Cheese", "Large", 150),
]

flavor = input("Select Flavor (Pepperoni/Ham & Cheese): ").lower()
size = input("Enter Size (Small, Medium, Large): ").lower()

found = False

for pizza in Pizza:
    if pizza[0].lower() == flavor and pizza[1].lower() == size:
        print("You Have Selected:", pizza[0])
        print("Size:", pizza[1])
        print("Pizza Price:", pizza[2])
        found = True
        break

if not found:
    print("Invalid Flavor or Size")















