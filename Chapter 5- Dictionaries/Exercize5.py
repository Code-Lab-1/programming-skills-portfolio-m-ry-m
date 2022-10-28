#Exercise 5: Pets
from unicodedata import name


pt={'Kind of animal':'Cat','name':'Kitty','Owner':'Nour'}
ppt={'Kind of anime':'Hamster','name':'Cucu','Owner':'Seba'}
ptt={'Kind of animal':'Snake','name':'snipet','Owner':'Afeefa'}
pets=[]
pets.append(pt)
pets.append(ppt)
pets.append(ptt)

for i in pets:
    print("\nI know about "+i['name'])
    for j,k in i.items():
        print('\t'+j+":"+k)