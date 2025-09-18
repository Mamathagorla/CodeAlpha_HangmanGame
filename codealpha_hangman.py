import random
words=["kai","barron","chloe","tim","maira"]
goal=random.choice(words)
guesslist=["_"]*len(goal)
attempts=0
temp=False
print("Welcome to Hangman!")
print("You have", 6-attempts, "attempts to guess the word.")
print(guesslist)

while(attempts<6):
  guess=input("Enter one letter of the word(a-z)=")
  found=False
  for j in range(len(goal)):
    if guess==goal[j]:
      guesslist[j]=guess
      print(guesslist)
      found=True
  if found==True:
      if "".join(guesslist)==goal:
        print("CONGRATS")
        temp=True
        break
      else:print("NICE TRY!,Guess next")
  else :
      attempts+=1
      if attempts==6:break
      else:print("OOPS! Try Again u have",(6-attempts),"more chances")
if temp==True:print("\U0001F389 YOU WON!")
else:print("\U0001F622 YOU LOST, The word is",goal)

