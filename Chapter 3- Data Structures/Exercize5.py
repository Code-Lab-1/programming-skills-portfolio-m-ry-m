#•Start with your program from Exercise 3-4. Add a print() call at the end of your 
# program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name 
# of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.

#Exercise 4: Change Guest List 
gst=['Tayyaba','Afeefa','Hadia','Wajeeha']
print('HEY',gst[0],'Isn\'t been ling since we met\?, Let\'s meet on dinner.')
print('HI',gst[1],'Didn\'t forget to invite you this time, let\'s meet up for dinner at my place')
print('WELCOME',gst[2],'Finally some free time,See you at dinner at my place')
print('YO',gst[3],'Another dinner invitation coming up, See you at my place')

gst.remove('Tayyaba')
gst.insert(0,'Hina')

print('\nHEY',gst[0],'Isn\'t been ling since we met\?, See you at dinner.')
print('HI',gst[1],'Didn\'t forget to invite you this time, let\'s meet up for dinner at my place')
print('WELCOME',gst[2],'Finally some free time,See you at dinner at my place')
print('YO',gst[3],'Another dinner invitation coming up, See you at my place')
