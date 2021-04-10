

#Question 1

'''I defined two lists; one contains the odd numbers, the other one contains the even numbers 1 to 10. 
After that, I merged two lists and named it "newlist". 
I created a new list called squares to be able to multiply all values in newlist by 2. 
Finally, I used for loop to print the data type of all values in the new list. '''


list_a=[1,3,5,7,9]
list_b=[2,4,6,8,10]
squares = []

newlist= list_a + list_b

squares = [i*2 for i in newlist]
print(squares)

for i in newlist:
    print(type(newlist))

