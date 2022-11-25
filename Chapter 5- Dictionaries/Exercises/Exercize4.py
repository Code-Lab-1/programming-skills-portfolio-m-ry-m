#Exercise 4: Rivers
river={'Congo':'Africa','Volga':'Russia','Amur':'China'}
for i,j in river.items():
    print('\n'+i+":"+j)
print('\nRivers in dictionary')
for i in river.keys():
    print('\n'+i)
print("\nCountries in dicctionary")
for i in river.values():
    print('\n'+i)