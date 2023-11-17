#Extend the list by adding another list
list=['1','5',['2',['8','10',['7']] ,'12'],'11']
list2=['17','18','20']
list[2][1][2].extend(list2)
print(list)