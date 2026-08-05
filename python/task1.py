import random 
posture = random.choice(["sitting", "standing"]) 
2 
direction = random.choice(["left", "right", "facing"]) 
distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance: {distance}")
def nexus(posture, direction, distance):
 if posture=="sitting":
  print("nexus stands up")
 if direction=="left" or direction=="right":
  print("nexus turns towards the door")
 while distance>0:
  print("moving ", distance," steps left")
  distance -=1
nexus(posture, direction, distance)