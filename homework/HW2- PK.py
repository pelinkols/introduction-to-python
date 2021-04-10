

#Homework Day2

#6,7,8,9,10,1,2,3,4,5

listem = ['1','2','3','4','5',
          '6','7','8','9','10']


print(list((listem[-5:]))+listem[:-5])
    

n=int(input("Please enter a single digit:"))
p=0

while not 0<n<10:
    print("please enter one digit number")
    n=int(input("Please enter a single digit:"))
    
    
for i in range(n+1):
    if i%2==0:
        print(i)
        p+=1
print("There are",p, "even numbers from O to",n)

