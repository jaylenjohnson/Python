class Amimal: 
	e= 'elephant'
	t= 'tiger'
	b= 'bat'
	w= 'wrong'
	def guess_who_am_i(user_input):
		if user_input== e:
			return e
		elif user_input == t:
			return t
		elif user_input== b:
			return b
		else
			return w



def main():
	Amimal_object = Amimal()
	userinput="0"
	ans = "x"
	print"I will give you 3 hints, guess what animal I am"
    while userinput !="w":
    	print "I have exceptional memory Who am I?:"
        userinput= raw_input()
        ans = Animal_object.guess_who_am_i(userinput)
        if  ans == Animal_object.e:
        	print "You got it! I am elephant."
        	break
        ans = Animal_object.guess_who_am_i(userinput)
        elif ans == Animal_object.t:
        	print "I am the biggest cat Who am I?:"






		

