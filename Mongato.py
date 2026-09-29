flavor = input("Select Flavor(Neopolitan/Meat Lover's/Pepperoni Fiesta):").lower()
if flavor == "neopolitan":
    print("You Have Selected Neopolitan")
elif flavor == "meat lovers":
    print("You Have Selected Meat Lover's")
elif flavor == "pepperoni fiesta":
    print("You Have Selected Pepperoni Fiesta")
else:
    print("invalid Flavor")

size = input("Enter Size(Small, Medium, Large):").lower()

if size == "small":
 price = 250
elif size =="medium":
 price = 350
elif size == "large":
 price = 450
else:
 price = 0
 print("Invalid Size")

if price > 0:
    print("Pizza Price:",price)