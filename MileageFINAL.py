from sys import exit
global ans
answer = "N"


# First function confirms that there is in fact a full tank
# before it begins, which is vital for the calculations
def fullTankBegin():
	fullTank = input("Do you have a full tank of gas? Y/N\n")
	if fullTank == "N":
		print("Please fill up the tank\nbefore beginning your trip!")
		print("-" * 20)
		fullTankBegin()
		# This leads to the function call of numtrips()
	else:
		print("Great! Let's begin")
		print("-" * 20)
	numTrips()	

# I decided to allow the user to input as many trips as they like
# The while loop calculates the odo reading and the mpg	
def numTrips():
	num = 1
	numTrip = 0
	odoInitial = int(input("What is the initial odometer reading before trip begins? "))
	ans = answer
	while ans == "N":
		print("Odometer reading after trip", num)
		odoStr = input("")
		odoInt = int(odoStr)
		print("How many gallons are needed to fill the tank after trip", num, "?")
		galStr = input("")
		galOdo = int(galStr)
		# This appends to the gallons[]
		gallons.append(galOdo)
		odoX = odoInt - odoInitial
		# After the math, it appends to the miles[]
		miles.append(odoX)
		odoInitial = odoInt
		odoMPG = odoX / galOdo
		# After the math, it appends to the MPG
		MPG.append(odoMPG)
		print("Your MPG on this fill up is:", odoMPG)
		num = num + 1
		numTrip = numTrip + 1
		print("Is your trip finished? ")
		ans = input("Y/N? ")
	# Final append puts the number of trips in the list.
	trips.append(numTrip)
	MPGTotals()
	ending()

# This function shows the final display of the totals.	
def MPGTotals():
	print("Total miles driven", sum(miles))
	print("Your overall trip MPG is: ", sum(miles) / sum(gallons))
	print("Your average MPG per fill up is: ", sum(MPG) / sum(trips))

def ending():
	print("Till next time, don't drive drunk!")
	answer = "Y"
	exit(0)
		
# The empty lists
trips = []
miles = []
gallons = []
MPG = []

# This function call initiates the program
fullTankBegin()


