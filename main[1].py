print("BMR calculator")
a = float(input("Enter your height in inches: "))
b = float(input("Enter your weight in pounds: "))
c = int(input("Enter your age in years: "))
d = input("Are you a woman or a man? ").lower()

if d == "man":
    bmr = 66 + (6.23 * b) + (12.7 * a) - (6.8 * c)
    print(f"BMR = {bmr}")
elif d == "woman":
    bmr = 655 + (4.35 * b) + (4.7 * a) - (4.7 * c)
    print(f"BMR = {bmr}")
else:
    print("Please enter 'man' or 'woman'.")
