#Exercize3 Print Date and Time
from datetime import date
td=date.today()
print('Today\'s Date: ',td)
from datetime import datetime
tm= datetime.now()
t= tm.strftime('%H : %M : %S')
print("Time: ",t)