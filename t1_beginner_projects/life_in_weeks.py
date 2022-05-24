age = int(input("What's your age?\n"))
max_age = int(input("At what age are you expecting your death?\n"))

remaining_years = max_age - age
days_left = remaining_years * 365
weeks_left = remaining_years * 52
months_left = remaining_years * 12
print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left...")
