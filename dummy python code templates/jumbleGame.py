import random

def choose():
	words=["water","tiger","soccer","biriyani","icecream","rainbow","puzzel","mafia","programming"]	
	select=random.choice(words)
	return select
	
def jumble(word):
	qn="".join(random.sample(word,len(word)))
	return qn

def thanks(p1,p2,s1,s2):
	print(p1,"'s score : ",s1)
	print(p2,"'s score : ",s2)
	print("Thank you for playing....Come again")

def play():
	p1=input("Enter the name of 1st player : ")
	p2=input("Enter the name of 2nd player : ")
	turn=0
	s1=0
	s2=0
	i=1
	while(i==1):
		if(turn%2==0):
			word=choose()
			qn=jumble(word)
			print(p1,"'s turn.")
			print(qn)
			u=input("Guess the word : ")
			if(u==word):
				s1=s1+1
				print("yo...you are Correct.")	
				print("Your score : ",s1,end="\n")
			else:
				print("oops :-( better luck next time",end="\n")
		if(turn%2==0):
			word=choose()
			qn=jumble(word)
			print(p2,"'s turn.")
			print(qn)
			u=input("Guess the word : ")
			if(u==word):
				s2=s2+1
				print("yo...you are Correct.")	
				print("Your score : ",s2,end="\n")
			else:
				print("oops :-( better luck next time",end="\n")	
		i=int(input("Want to continue? (1 for yes/0 for no) : "))
	thanks(p1,p2,s1,s2)	

play()		
