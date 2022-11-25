#Now using last question add Fail for -45 marks and A+ grade for 80+ marks

num=int(input("Enter your marks: "))
if num>=80:
    print("You got an A+ grade.")
elif num>=70 and num<80:
    print("You have an A grade.")
elif num>=60 and num<70:
    print("You got a B grade.")
elif num>=45 and num<60:
    print("You got a C grade.")
else:
    print("You failed.")