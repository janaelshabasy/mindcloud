import time
minutes = int(input("Enter test minutes: ")) 
seconds = int(input("Enter test seconds: ")) 

if seconds>59 or (minutes==0 and seconds==0) or minutes<0 or seconds<0:
 print("Invalid test duration")

else:
 
 if (minutes==5 and seconds>0) or minutes>5:
  print("Safety limit exceeded! Test duration capped to 05:00")
  minutes=5
  seconds=0

 total_seconds= seconds + minutes*60

 #live countdown
 while True:
  mins= total_seconds //60
  secs= total_seconds %60
  print(mins,":",secs)

  if total_seconds>30:
   print("POWER ON | Remaining: ",mins,":",secs)
  else:
   if total_seconds>10:
     print("STABILIZING SYSTEM | Remaining: ",mins,":",secs)
   elif total_seconds<=10:
     print("COOLDOWN PHASE | Do not touch | ",mins,":",secs)

  if total_seconds==0:
   print("Power test completed successfully")
   break
  time.sleep(1)
  total_seconds -=1