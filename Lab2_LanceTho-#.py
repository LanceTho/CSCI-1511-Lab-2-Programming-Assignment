#Restaurant Tip Calculator
#Lance Thongsavanh
#As a restaurant owner, you need a program that calculates tip suggestions for your customers.
#1/23/2026

#Declares variables
bill: float = 0
prompt: str = "Please enter the total of a dinner bill (exclude the '$')"
error: str = "Invalid total"
recipt_total: str = "TOTAL:"
recipt_15: str = "15%:"
recipt_20: str = "20%:"
tip_15: float = 0
tip_20: float = 0

#Prompts the user for the bill and loops if the user provides an invalid value
print(f"{prompt:<{20}}")
bill = float(input())
while(bill <= 0):
    print(f"{error:{20}}")
    print(f"{prompt:{20}}")
    bill = float(input())

#Calculates tip for 15% and 20%
tip_15 = bill*0.15
tip_20 = bill*0.2

#Outputs the total
print(f"|{recipt_total:<{10}}" + f"${bill:.2f}|")

#Outputs the 15% tip and total with it added
print(f"|{recipt_15:<{11}}" + f"${tip_15:.2f}|")
print(f"|{recipt_total:{10}}" + f"${(bill + tip_15):.2f}|")

#Outputs the 20% tip and total with it added
print(f"|{recipt_20:<{10}}" + f"${tip_20:.2f}|")
print(f"|{recipt_total:{10}}" + f"${(bill + tip_20):.2f}|")