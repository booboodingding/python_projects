# I'm using global variables because it's easier for this project
# Two lists will be created and appended to
global cust
cust = []
global bal
bal = []

# This function decides if the input name is in the list.
# It begins the customer cycle.
def changeCust():
	global currentCustInd
	custname = input("What is your name? ")
	if custname not in cust:
		print("Name not found, try again.")
		changeCust()
	if custname in cust:
	# index turns the index into an integer for use later
		currentCustInd = cust.index(custname)

# This function asks for deposit amount, and adds it to bal[]			
def deposit():
	global currentCustInd
	print("How much to deposit? ")
	depAmt = int(input())
	bal[currentCustInd] = depAmt + bal[currentCustInd]

# This function subtracts from the bal	
def withdrawl(person):	
	global currentCustInd
	print("How much to withdrawl? ")
	withdAmt = int(input())
	if withdAmt > bal[person]:
		print("You don't have sufficient funds. Try again.")
		withdrawl(person)
	else:
		bal[person] = bal[person] - withdAmt

# This variable is altered by changecust() function
global currentCustInd	
currentCustInd = 0	

# This input begins the module. It decides the amount of customers
custNumInt = int(input("How many customers? "))

# The for loop asks for the names to be placed in cust[]
nums = 1
for i in range(custNumInt):
	print("Name of customer", nums, "?")
	nums = nums + 1
	custName = input("")
	cust.append(custName)
	print("Starting balance for", custName, "?")
	# I decided to ask the user how much to start with at the
	# beginning. It makes the program more dynamic
	custStart = int(input())
	bal.append(custStart)
		
changeCust()

# This while loop is the menu that is constantly on the screen after
# every function call. It supplies the user with options, as well
# as initiates all of the different functions

ans = ""
while ans != "Y":
	print("What would you like to do today?")
	print("Type D to deposit money\nType W to withdraw money")
	print("Type B to display balance\nType C to change user")
	print("Type E to exit")
	choice = input("")
	if choice == "D":
		print("Deposit it is!")
		deposit()
	elif choice == "W":
		print("Withdrawl it is!")
		withdrawl(currentCustInd)
	elif choice == "B":
		print(cust[currentCustInd], ", your balance is:")
		print("-" * 10, bal[currentCustInd], "-" * 10)
	elif choice == "C":
		print("Changing customer now...")
		changeCust()
	elif choice == "E":
		ans = "Y"
		print("Goodbye")
	
