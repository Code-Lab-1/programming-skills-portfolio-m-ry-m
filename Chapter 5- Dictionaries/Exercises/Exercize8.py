#Let each person have atleast 3 favorite numbers
peep={'Ali':[3,2,1],'Asma':[4,2,2],'Usman':[6,3,1],'Maimonah':[7,4,3],
'Ayesha':[8,5,3],'Sumairah':[9,6,2]}

for name, num in peep.items():
    print('\n',name.title(),'likes:')
    for i in num:
        print(' ',i)