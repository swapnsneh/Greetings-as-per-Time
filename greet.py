from datetime import *

now = datetime.now()
print(now)
print(now.hour)

hour= now.hour
if hour <= 12:
    print("Good Morning Sir")

elif 12< hour  <=17:
    print("Good Afternoon Sir")
elif 17< hour  <19:
    print("Good Evening Sir")
else:
    print("Good Night Sir")
