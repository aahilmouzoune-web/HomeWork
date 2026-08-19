print("Hello! I am a AI Bot. What is your name? :")
#Get user Input
name=input()
#Respond to the user's name
print(f"Nice to meet you,{name}!")
#Ask a Question
print("How are you feeling today?(Good/Bad):")
mood=input().lower()
#Use coditional Statement To Respond Based On Input
if mood=="good":
    print("I am glad to hear that!")
    print("How is the weather(Sunny,Rainy,Windy)")
    weather=input().lower()
elif mood=="Bad":
    print("I am sorry tohear that.Hope things get better soon.")
else:
    print("I see somtimes it's hard to put fellings into words")
    print("How is the weather(Sunny,Rainy,Windy)")
    weather=input().lower()
    if weather =="Sunny":
        print("I am glad to hear that")
    elif weather =="Rainy" or weather =="Windy":
        print("I hope the weather gets better")
    else:
        print("I hope the weather gets better")
print(f"It was nice chatting with you {name}.Goodbye")