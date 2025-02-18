# Python compound interest calculator
# A = P(1 + (r/n)^t

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero")
        
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
        
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

print()        
print(f"Principal: {principal}")
print(f"Rate: {rate}")
print(f"Time in years: {time}")

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): ${total:.2f}\n")