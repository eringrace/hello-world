####################### TRAVELERS #######################

def travelers(people):
	if people.isdigit():
		people = int(people)
		return people
	else:
		people = raw_input("\nSorry, I only understand numerals and decimals. So how many people are going?")
		return travelers(people)

####################### FLIGHT #######################


####################### DAYS #######################
def duration(days):
	if days.isdigit():
		days = int(days)
		return days
	else:
		days = raw_input("\nSorry, I only understand numerals and decimals. So how many people are going?")
		return duration(days)

####################### MEALS #######################
# Breakfast subtracts one meal, since flights from the US don't arrive in the morning.
# Dinners subtracts one meal, since flights to the US leave before dinner.

def meals():
    breakfast = (750 * duration(days)) - 750 
    breakfast = breakfast - 750
    lunch = 1500 * duration(days)
    dinner = 2000 * duration(days)
    dinner = dinner - 2000
    meal_cost = breakfast + lunch + dinner
    return meal_cost

####################### ACCOMODATION #######################
# This section doesn't work right with exception output

def accomodation(acc_var):
	if acc_var == "1":
		return 8500 * duration(days)
	elif acc_var == "2":
		return 4500 * duration(days)
	elif acc_var == "3":
		return 3000 * duration(days)
	else:
		acc_var = raw_input("\nSorry, I wasn't clear. If you want to stay in a hotel, press 1; if you want to stay in a guest house, press 2; and if you want to stay in a hostel, press 3.")
		return accomodation(acc_var)

####################### TRAVEL #######################

print "So you're going to Japan! Okay..."
people = raw_input("\nHow many travelers are there?")
print "\nGreat! That's %s travelers." % travelers(people)
print "\nNext we'll look at the flight cost."
days = raw_input("\nHow many days do you want to stay?")
print "\nGreat! That's %s days." % duration(days)
print "\nThat'll be about %s yen in meals..." % (meals())
acc_var = raw_input("\nWhat kind of accomodations do you want?\n     If you want to stay in a hotel, press 1.\n     If you want to stay in a guest house, press 2.\n     If you want to stay in a hostel, press 3. \n")
print "\nSo you'll spend about %s on accommodations..." % (accomodation(acc_var))
