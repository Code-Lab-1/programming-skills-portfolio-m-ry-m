#Print a python program to print dictioanry in table format
dicto={'A':[9,8,7],'B':[6,5,4],'C':[3,2,1]}
for row in zip(*([key]+(value) for key, value in sorted(dicto.items()))):
    print(*row)