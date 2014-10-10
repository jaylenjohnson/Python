print ("Welcome to the guessing game\n")

guess=0

min=1
max=100
mid= (min + max) // 2

name = raw_input("Hi, what is your Name? ")
print("Hello " + name + "," + " Lets Play a Game!")
print("Think of random number from 1 to 100, and I'll try to guess it!\n")

userinput="no"
while userinput !="yes":
	randomanswer= mid
	print(" I guessed " + str(randomanswer))
	userinput= raw_input(" Is this your number ") 
	if userinput == "no":
		response2= raw_input("Is it greater? ")
		if response2== "yes":
			min = randomanswer +1
			mid = mid = (min+max) /2
			guess += 1
			
		elif response2 == "no":
			max = randomanswer -1
			mid = (min+max) // 2
			guess += 1
	elif userinput =="yes":
		print("Yeey! I got it in " + str(guess) + " tries !\n")	
		Playmore = raw_input("Do you want to play more? ")
		if Playmore == "no":
    			print("Bye-bye")
		    	userinput = "yes"
		else:
		    	continue




 I guessed 50
 Is this your number no
Is it greater? no
 I guessed 25
 Is this your number no
Is it greater? no
 I guessed 12
 Is this your number no
Is it greater? yes
 I guessed 18
 Is this your number no
Is it greater? yes
 I guessed 21
 Is this your number yes
Yeey! I got it in 4 tries !

Do you want to play more? no
Bye-bye








