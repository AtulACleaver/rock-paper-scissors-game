import random


def rpc():
    options = ["Rock", "Paper", "Scissors"]
    me = input("\nYour choice(Rock, Paper, Scissors): ")
    bot = random.choice(options)

    if me.lower() == bot.lower():
        print(f"\nYou chose {me} and the bot chose {bot}. Tied!")

    elif me.lower() == 'rock':
        if bot.lower() == 'scissors':
            print(f"\nYou chose {me} and the bot chose {bot}. You win!!")
        elif bot.lower() == 'paper':
            print(f"\nYou chose {me} and the bot chose {bot}. You lose!!")

    elif me.lower() == 'paper':
        if bot.lower() == 'rock':
            print(f"\nYou chose {me} and the bot chose {bot}. You win!!")
        elif bot.lower() == 'scissors':
            print(f"\nYou chose {me} and the bot chose {bot}. You lose!!")

    elif me.lower() == 'scissors':
        if bot.lower() == 'paper':
            print(f"\nYou chose {me} and the bot chose {bot}. You win!!")
        elif bot.lower() == 'rock':
            print(f"\nYou chose {me} and the bot chose {bot}. You lose!!")
    yn = input("\nDo you want to play rock paper scissors?(Yes/No) ")
    if yn.lower() == 'yes':
        rpc()
    elif yn.lower() == 'no':
        print("\nHave a good day, then!")
    else:
        print("Try again!")


play = input("\nDo you want to play rock paper scissors?(Yes/No) ")

if play.lower() == 'yes':
    rpc()
elif play.lower() == 'no':
    print("Have a good day, then!")
else:
    print("Try again!")
