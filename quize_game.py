print("Welcome to Quiz!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

score =0
print("Okay lets start !")

ans = int( input("How many unit are in a dorzen? "))
if ans == 12  :
    print("Correct!")
    score+=1
else:
    print("No it's Incorrect")
    

ans = int( input("How many meter in a kilometer? "))
if ans == 1000  :
    print("Correct!")
    score+=1
else:
    print("No it's Incorrect")
    
    
ans =  input("Which is Bigger Unit Terabytes or Gigabytes? ").lower()
if ans == "terabytes"  :
    print("Correct!")
    score+=1
else:
    print("No it's Incorrect")

ans =  input("What is the mixture of of Copper and Zinc ").lower()
if ans == "brass"  :
    print("Correct!")
    score+=1
else:
    print("No it's Incorrect")
    
print("You got "+ str(score)+" question correct!")
print("You got "+ str(score/4*100)+" question correct!")