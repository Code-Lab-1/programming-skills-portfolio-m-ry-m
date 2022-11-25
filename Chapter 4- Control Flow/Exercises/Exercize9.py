#Add some more items to the menu and print their choices
menu=input('Would you like tea, coffee, americano or latte?')
if menu=='tea' or menu=='Tea' or menu=='TEA':
    print('Preparing tea...')
elif menu=='coffee' or menu=='Coffee' or menu=='COFFEE':
    print('Preparing coffee...')
elif menu=='Americano' or menu=='americano' or menu=='AMERICANO':
    print('Preparing Americano...')
elif menu=='latte' or menu=='Latte' or menu=='LATTE':
    print('Preparing latte...')