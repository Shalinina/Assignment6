def con_in_lit(gallons):
    gal_in_liters = gallons*3.785
    return gal_in_liters
gallons = float(input("Enter the Quantity of gasoline in gallons "))
if gallons > 0:
 gal_in_liters = con_in_lit(gallons)
 print("The Quanitity in Liters of Gallons is: " + str(gal_in_liters))
else:
    print("You Entered a Negative Number")

