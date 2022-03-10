twelveTime = input("Enter time in 12hrs clock with hh:mm:ss(AM/PM): ").split()

for time in twelveTime:
    hours, mins, secs = [i for i in time.split(":")]

dur = secs[2:]
secs = secs[:2]
if dur=="PM":
    hours = str(int(hours) + 12)
    print("The converted time is: " + hours + ":" + mins + ":" + secs)

else:
    print("The converted time is: " + hours + ":" + mins + ":" + secs)
