#Print a table of a number
o=int(input("Enter a number: "))
def table(n):
  i=1
  while i<=10:
    k=n*i
    print(n,"x",i,"=",k)
    i+=1
table(o)