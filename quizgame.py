# Small project of a quiz game made to use the if and else statements.
# Coded by João Pedro Mendes Fernandes (chaosjpmendes@gmail.com)
# github.com/Jpfernandesm

print("Welcome to my computer quiz!")

playing = input("Do you want to play? " )


if playing.lower() != "yes":
    quit()
    
print("Okay, let's play!")
score = 0

answer = input("What does CPU stand for? " )
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")
  
  
  answer = input("What does GPU stand for? " )
if answer.lower() == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")
  
  
  answer = input("What does RAM stand for? " )
if answer.lower() == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")
  
  
  answer = input("What does PSU stand for? " )
if answer.lower() == "power supply":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")
  
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

     
    
