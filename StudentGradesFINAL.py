# Five empty lists

students = []
score1 = []
score2 = []
score3 = []
grades = []

# This function records the three test scores of each student
def tests():
	for i in students:
		print("What is the score for test #1 for", i, "?")
		test1 = int(input())
		score1.append(test1)
		print("What is the score for test #2  for", i, "?")
		test2= int(input())
		score2.append(test2)
		print("What is the score for test #3 for", i, "?")
		test3 = int(input())
		score3.append(test3)

# After tests(), this function then calculates the average based
# on the three test scores		
def scores1():
	for i in students:
		# I used index() because it was the most simple way for 
		# me to assign an index number to a variable
		stux = students.index(i)
		total = (score1[stux] + score2[stux] + score3[stux]) / 3
		# After the math, the grades are appended to grades[]
		grades.append(total)
		# The final display output depends on the total in if 
		# conditions
		print(i, "'s test average is", total)
		if total >= 90:
			print("The grade for", i, "is: A")
		elif total <90 and total >= 80:
			print("The grade for", i, "is: B")
		elif total < 80 and total >=70:
			print("The grade for", i, "is: C")
		elif total < 70 and total >= 60:
			print("The grade for", i, "is: D")
		else:
			print("The grade for", i, "is: F")
		

# I decided to allow the user to input the amount of students.			
studAmt = int(input("How many students? "))

nums = 1
# The user can input the name of the students
for i in range(studAmt):
	print("Name of student", nums, "?")
	nums = nums + 1
	studName = input("")
	# The names get appended to students[]
	students.append(studName)

# the function call for tests() after the for loop	
tests()
scores1()

#print(score1, score2, score3)
