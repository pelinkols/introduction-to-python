


#Final Project

comp= {"Q1":'Paris','Q2':'Tac Mahal',
       'Q3':'1789','Q4':'Picasso','Q5': 'Ankara','Q6':'Macron',
       'Q7':'Heart', 'Q8':'A', 'Q9': 'Kuala Lumpur','Q10':'Istanbul'}
answerList =[]
count=1

points=0
A1= str(input("Which city is known as the city of love? : "))
answerList.append(A1)
A2= str(input(" One of the 7 wonders of the world (in İndia)? : "))   
answerList.append(A2)
A3= str(input("Year of French revolution? : "))
answerList.append(A3)
A4= str(input("Who painted the Guernica painting?:"))
answerList.append(A4)
A5= str(input("Capital city of Turkey?: "))
answerList.append(A5)
A6= str(input("What is the surname president of France?: "))
answerList.append(A6)
A7= str(input("Which organ pumps blood?:"))
answerList.append(A7)
A8= str(input("what is the first letter of alphabet:"))
answerList.append(A8)
A9= str(input("what is the capital city of Malaysia:"))
answerList.append(A9)
A10= str(input("Most populated city of Turkey:"))
answerList.append(A10)

for answer in answerList:
    questionNumber= "Q"+str(count)
    
    if answer in comp[questionNumber]:
        points+=10
    count+=1

print(points)


if points<=50:
    print("You lost!")
    
else:
    print("You won!!")


