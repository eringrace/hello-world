####################### TRAVELERS #######################
def travelers(people):
	if people.isalpha() == True:
		people = raw_input("\nSorry, I only understand numerals and decimals. Try again. How many people are going?")
		return people
		travelers(people)
	else:
		people = int(people)
		return people
		print "\nGreat! That's %s travelers. Next we'll look at the flight cost." % (people)

####################### FLIGHT #######################

def	flight(ticket, people):
	if ticket.isalpha() == True:
		ticket = raw_input("\nSorry, I only understand numerals and decimals. Try again! How much is the ticket? (Don't include a dollar sign.)")
		return ticket
		flight()
	else:
		ticket = int(ticket)
		return ticket

####################### MEALS #######################
# Breakfast subtracts one meal, since flights from the US don't arrive in the morning.
# Dinners subtracts one meal, since flights to the US leave before dinner.

def meals():
    breakfast = (750 * days) - 750 
    breakfast = breakfast - 750
    lunch = 1500 * days
    dinner = 2000 * days
    dinner = dinner - 2000
    meal_cost = breakfast + lunch + dinner
    return meal_cost

####################### ACCOMODATION #######################
# This section doesn't work right with exception output

def accomodation(acc_var):
	if acc_var == "1":
		return 8500 * days
	elif acc_var == "2":
		return 4500 * days
	elif acc_var == "3": 
		return 3000 * days
	else:
		acc_var = raw_input("\nSorry, I wasn't clear. If you want to stay in a hotel, press 1; if you want to stay in a guest house, press 2; and if you want to stay in a hostel, press 3.")
		return accomodation(acc_var)

####################### TRAVEL #######################


print "So you're going to Japan! Okay..."

people = raw_input("\nHow many travelers are there?")
travelers(people)

ticket = raw_input("\nThe flight is the hard part. Go to Google Flights (google.com/flights) and find the cheapest one you can for the dates you want, then enter it here.")
flight(ticket, people)
print "\nOkay, that's $%s in total (%s per person)..." % (ticket * people, ticket)

days = int(raw_input("How many days do you want to stay in Japan?"))
print "\nThat'll be about %s yen in meals..." % (meals())

acc_var = raw_input("\nWhat kind of accomodations do you want?\n     If you want to stay in a hotel, press 1.\n     If you want to stay in a guest house, press 2.\n     If you want to stay in a hostel, press 3. \n")
print "\nSo you'll spend about %s on accommodations..." % (accomodation(acc_var))

# When it comes time to do totals, break up the amounts by cost type (meals, etc) and also per-person cost for the total and each
# cost type. Add an if statement, however, that detects whether there's only one person going on the trip and, if so, removes the 
# per-person cost element.
