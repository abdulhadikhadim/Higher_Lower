from game_data import data
import random
from art import logo, vs
import os

def format_data(account):
    '''Takes the data from the Data and return the information'''
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{acc_name} a {acc_desc} from {acc_country}"

def check_answer(guess , a_follower , b_follower):
    if a_follower > b_follower:
        return guess =="a"
    else:
        return guess == "b"
def game():
    print(logo)
    score = 0
    is_game_ended = False
    option_a = random.choice(data)
    option_b = random.choice(data)

    while not is_game_ended:
        option_a = option_b
        option_b = random.choice(data)
        print(f"Option A is {format_data(option_a)}")
        print(vs)
        print(f"Against B is {format_data(option_b)}")
        guess = input("Which has the more followers: Type a/b:").lower()
        a_follower = ['follower_count']
        b_follower = ['follower_count']
        is_correct = check_answer(guess , a_follower,b_follower)
        # clear()
        os.system('cls')
        print(logo)
        if is_correct == True:
            score+=1
            print(f"You Win and your current score is {score}")
        else:
            print(f"Sorry Wrong answer You! Your Final Score is {score}")
            is_game_ended = True
    input("Type Any key to exit")

game()