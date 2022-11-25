#Define a function that accepts roll number and 
# returns whether the student is present or absent.
def det(roll):
    x = [23,43,22,56]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("Enter roll no. "))
det(roll)