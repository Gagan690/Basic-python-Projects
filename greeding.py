import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if timestamp < 12:
     print("good Moring")
elif timestamp > 12 and timestamp <= 16:
     print("Good Afternoon")
elif timestamp > 16 and timestamp <= 20:
     print ("good Evening")
else :
     print("Good Night")