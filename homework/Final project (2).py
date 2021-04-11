


#Final Project

comp= {"Which city is known as the city of love?  ":'Paris',"One of the 7 wonders of the world (in İndia)? ":'Tac Mahal',
       "Year of French revolution?  ":'1789',"Who painted the Guernica painting? ":'Picasso',
       "Capital city of Turkey? ": 'Ankara',"What is the surname president of France? ":'Macron',
       "Which organ pumps blood?":'Heart', "what is the first letter of alphabet ":'A', 
       "what is the capital city of Malaysia ": 'Kuala Lumpur',"Most populated city of Turkey ":'Istanbul'}

points=0

for question in comp.keys():
    print(question)
    answer=input("Answer: ")
    if answer in comp[question]:
        points+=10
    

print(points)


if points<=50:
    print("You lost!")
    
else:
    print("You won!!")


