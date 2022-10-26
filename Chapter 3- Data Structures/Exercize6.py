#Exercise 6: Shrinking Guest List 
gst=['Tayyaba','Afeefa','Hadia','Wajeeha']
print('HEY',gst[0],'Isn\'t been ling since we met\?, Let\'s meet on dinner.')
print('HI',gst[1],'Didn\'t forget to invite you this time, let\'s meet up for dinner at my place')
print('WELCOME',gst[2],'Finally some free time,See you at dinner at my place')
print('YO',gst[3],'Another dinner invitation coming up, See you at my place')

print("Unfortunately,Tayyaba can't make it to dinner.")
gst.remove('Tayyaba')
gst.insert(0,'Hina')

print('\nHEY',gst[0],'Isn\'t been ling since we met\?, See you at dinner.')
print('HI',gst[1],'Didn\'t forget to invite you this time, let\'s meet up for dinner at my place')
print('WELCOME',gst[2],'Finally some free time,See you at dinner at my place')
print('YO',gst[3],'Another dinner invitation coming up, See you at my place')

print("\nSorry, we can only invite two people to dinner.")
print("Sorry, " + gst[3] + " there's no room at the table.")
gst.pop()
print("Sorry, " + gst[2]+ " there's no room at the table.")
gst.pop()

print(gst[0] + ", please come to dinner.")
print(gst[1] + ", please come to dinner.")

print(gst)