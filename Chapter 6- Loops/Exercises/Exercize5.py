#Exercise 5: No Pastrami 
sandwich_orders=['Club sandwich','Pastrami','Chicken sandwich','Pastrami','Nutella Sandwich',
'Grill chicken sandwitch','Seafood sandwich','Pastrami','Ham sandwich']
print("Deli has run out of Pastrami")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

finished_sandwiches=[]
while sandwich_orders:
    mkng=sandwich_orders.pop() 
    finished_sandwiches.append(mkng)
print('\n')
for i in finished_sandwiches:
    print('Your',i,'is made')