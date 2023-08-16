# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_years = (90 - int(age))
balance_days = 365 * remaining_years
balance_weeks = 52 * remaining_years
balance_months = 12 * remaining_years

print(f"You have {balance_days} days, {balance_weeks} weeks, and {balance_months} months left")