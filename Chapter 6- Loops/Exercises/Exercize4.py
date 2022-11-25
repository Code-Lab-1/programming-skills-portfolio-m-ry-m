#Exercise 4: Deli
sandwich_orders=['Club sandwich','Chicken sandwich','Nutella Sandwich',
'Grill chicken sandwitch','Seafood sandwich','Ham sandwich']
finished_sandwiches=[]
while sandwich_orders:
    mkng=sandwich_orders.pop()
    print("I'm making your",mkng)   
    finished_sandwiches.append(mkng)
print('\nYour:-')
for i in finished_sandwiches:
    print(i,'is made')