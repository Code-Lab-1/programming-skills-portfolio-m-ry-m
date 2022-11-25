#Exercise 2: Movie Tickets
i=1
while i>0:
    age=int(input('Enter your age: '))
    if age<3:
        print("You're ticket is free")
    elif age>=3 and age<12:
        print("You're ticket is $10")
    else:
        print("You're ticket is $15")