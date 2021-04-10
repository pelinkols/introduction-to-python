
#User login application

username= 'pelink'
passcode= 2323

username= str(input("Please enter your username:"))
passcode= int(input("Please enter your password: "))

if username=='pelink' and passcode==2323:
    print("You sucessfully entered your account!")
    
elif username!='pelink' and passcode==2323:
    print("Your username is wrong!!!")
    
elif username=='pelink' and passcode!=2323:
    print("Your passcode is wrong!!!")
    
elif username!='pelink'and passcode!=2323:
    print("your passcode and username are wrong.")
    
    
    
#extra part

u = {'username':'pelink'}
     
p = {"passcode":"2323"}

username= str(input("Please enter your username:"))
passcode= str(input("Please enter your password: "))

if username in u.values():
    if passcode in p.values():
        print("you entered succesfully.")
    else: 
        print("Your passcode is wrong!!!")
        
else :
    if passcode in p.values():
        print("Your username is wrong!!!") 
    else: 
        print("your passcode and username are wrong.")
    

    