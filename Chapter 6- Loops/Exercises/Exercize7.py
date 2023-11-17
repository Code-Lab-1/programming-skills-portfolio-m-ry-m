#Print the table of a number as their power increase
o=int(input("Enter a number: "))
def table(n):
  i=1
  while i<=10:
    k=n**i
    print(n,"^",i,"=",k)
    i+=1
table(o)