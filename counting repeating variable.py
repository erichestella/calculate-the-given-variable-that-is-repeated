#adding some title 
print('\nCOUNTING THE VARIABLE THAT IS REPEATING:')

#putting some display 
print('\nGiven: Nicole is such a cutie. Nicole is soft masc. Nicole is shorter than me. Nicole is very funny person. \nNicole is my crush in BSCPE 1-4. Nicole likes to go to different places. Nicole is very pretty. Nicole is smart. \nNicole is my one and lowkey crush.\n ')

#these are the variable  
type_name = 'Nicole is such a cutie. Nicole is soft masc. Nicole is shorter than me. Nicole is very funny person. \nNicole is my crush in BSCPE 1-4. Nicole likes to go to different places. Nicole is very pretty. Nicole is smart. \nNicole is my one and lowkey crush.\n '
find = 'Nicole' 

#these are the variable that defines the counting of the variable 
counting_variable = 0 
start = 0

#this function identify how many of the variable are repeated
while True:
    numbers = type_name.find(find, start)
    if numbers == -1:
        break
    counting_variable += 1
    start = numbers + len(find)

#it displays the result of how many times the given is repeated
print('RESULT: \n The given variable', find, 'appears to have repeated', counting_variable, 'times')