#Input student marks and grade them as
#grade A = 70+ marks
#grade B = 60+ marks
#grade C = 45+ marks
num=int(input("Enter your marks: "))
if num>=70:
    print("You have an A grade.")
elif num>=60 and num<70:
    print("You got a B grade.")
elif num>=45 and num<60:
    print("You got a C grade.")