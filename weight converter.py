
unit=input("ENTER THE WEIGHT IN KILOGRAM OR POUNDS(K/L) ")
weight=float(input("Enter the weight: \n"))
if unit =="K":
    weight = weight * 2.205
    unit= "Lbs"
    print(f"The weight is {round(weight,2)}{unit} ") 
elif unit =="L":
    weight = weight / 2.205
    unit= "Kg"
    print(f"The weight is{weight}{unit} ") 
else:
    print(f"The unit {unit} is invaild please enter a vaild unit")