# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if principle <= 0:
        print("Interest rate cannot be less than or equal to zero")
    else:
        break
while True:
    time = float(input("Enter the time in years: "))
    if principle <= 0:
        print("Time cannot be less than or equal to zero")
    else:
        break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)

print(f"The Balance after {time} years : Kshs{total:.2f}")
