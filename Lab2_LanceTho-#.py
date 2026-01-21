#Restaurant Tip Calculator
#Lance Thongsavanh
#As a restaurant owner, you need a program that calculates tip suggestions for your customers.
#1/21/2026

#Requirements:
#Prompt the user for the total of a dinner bill
#Calculate a 15% tip and a 20% tip
#Print the suggested tip amounts
#Print the total bill amount including the 15$ tip, and then again with the 20% tip
#You must use f-strings for all output
#Currency should be correctly displayed

bill: float = 0
width: int = 20
prompt: str = "Please enter the total of a dinner bill"
error: str ="Invalid total"
tip_15: float = 0
tip_20: float = 0

print(f"{prompt:{width}}:")
bill = float(input())
while(bill <= 0):
    print(f"{error:{width}}")
    print(f"{prompt:{width}}:")
    bill = float(input())

tip_15 = bill*0.15
tip_20 = bill*0.2

print(f"15% tip: ${tip_15:.2f}")
print(f"20% tip: ${tip_20:.2f}")