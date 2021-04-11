import operator
notes= {}

for student in range (5):
    name=str(input("please enter the student name: "))
    m=int(input("please enter midterm grade:"))
    p=int(input("please enter project grade:"))
    f=int(input("please enter final grade:"))
    
    passing_grade= m*0.3 + p*0.3 + f*0.4
    notes[name]= format(passing_grade, ".2f")
    print(format(passing_grade, ".2f"))
    

print(dict(sorted(notes.items(), key=operator.itemgetter(1),reverse=True)))
      
      

        

