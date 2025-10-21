# Python Quiz Game :

questions = ('How many elements are their in a periodic table ?',
             'How many bones are there in an adult human body ?',
             'What is the most abundant gas in earth\'s atmosphere',
             'Which animal lays the largest egg?',
             'Which planet in the solar system is the hottest?')

options = (('A.70','B.118','C.135','D.108'),
           ('A.306','B.206','C.300','D.302'),
           ('A.Nitrogen','B.Oxygen','C.Hydrogen','D.Carbon Dioxide'),
           ('A.Whale','B.Shark','C.Giraffe','D.Ostrich'),
           ('A.Mars','B.Mercury','C.Venus','D.Jupiter'))

answers = ('B','B','A','D','C')

guesses = []
score = 0
Ques_no = 0


for question in questions :
    print(question)
    for option in options[Ques_no] :
        print(option, end=' ')
        print()
    guess = input('Enter your Guess (A,B,C,D) : ')  
    guesses.append(guess)
    if guess == answers[Ques_no].upper():
        score+=1
        print('CORRECT')
    else :
        print('INCORRECT')       
        print(f'The correct answer is {answers[Ques_no]}')   
    Ques_no+=1
    
    print('__________________________________________________________________________')

print('__________________________RESULT_________________________')
print('ANSWERS : ',end='')
for answer in answers :
    print(answer, end=' ')

print()

print('GUESSES : ', end='')
for guess in guesses:
    print(guess, end=' ')

print()

score = int(score/len(questions)*100)
print(f'Your final score is : {score} Points')