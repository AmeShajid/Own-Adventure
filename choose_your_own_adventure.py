#this is basically like pick a path and see where it leads you its fr nice
#user can pick anything and it will lead them somewhere else

#first ask them for their name
name = input("Enter your name: ")
print(f"Welcome {name} to the world of my imagination")# welcome them to your game

#start your adventure
# .lower on all questions so easier to track inputs
answer = input("Alright bro so first thing first lets test your morals and ethics. Train is coming towards a family and a singular man. On the left there is a family of 4 and on the right its a single man. Which way will you pull the lever... Left or Right.: ").lower()#over here add lower so its easier to code out the outputs

if answer == "left":# if our answer is left then we will ask them a murderous question...
    answer == input("Hmm okay I see you little killer. Your punishment is... Will you run across legos or swim in lava? Legos or Lava: ").lower()# here is another prompt

    if answer == "legos":# if answer is legos then..
        print("Okay I see you a little munch. Real men aren't scared to swim in lava")

    elif answer == "lava":# if answer is lava then....
        print('You are suicidal bruh wassup with you smh')

    else:#if they don't type something valid
        print("Bruh I asked you for lava or legos stop being a little bich fr")

elif answer == "right":# if your answer is right lets continue
    answer = input("You think Ame Jahan Shajid is a very handsome boy? Yes or No: ").lower()#other prompt

    if answer == "yes":# if answer is yes
        print("Wow very good choice! Go make your own game now!")
    elif answer =="no":# if answer is no
        print("yeah game over little sht")
    else:# end game!
        print("bye.")
else:
    print("Mf I said left or right. You lose bruh go away.")

print("Thanks for playing!")

# you can keep on going on forever and ever. I will keep it short, you can even add a point system too for every option but yk yuh











