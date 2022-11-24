#Print menu and ask if the user would like to know the prices
menu='Menu: \nAmericano\nCoffee\nLatte\nEspresso\nTea\nMocha'
print(menu)
ask=input("\nWould you like to know the prices?")
if ask=='yes' or ask=='YES' or ask=='Yes':
    print('Menu: \nAmericano $3\nCoffee $2.5\nLatte $5\nEspresso $5\nTea $2\nMocha $5')