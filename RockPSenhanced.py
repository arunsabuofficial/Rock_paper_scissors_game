#!/usr/bin/env

import random;
from enum import IntEnum;

class Action(IntEnum):
     Rock=0
     Paper=1
     Scissors=2

def get_user_selection():
    choices=[f"{action.name}[{action.value}]" for action in Action];
    choices_str=", ".join(choices)
    selection=int(input(f"enter  choice ({choices_str}): "))

    action=Action(selection)
    return action

def computer_selection():
    selection=random.randint(0,len(Action)-1)
    action= Action(selection);
    return action;

def determine_winner(user_action,computer_action):
    victories={
        Action.Paper: [Action.Rock],
        Action.Rock: [Action.Scissors],
        Action.Scissors: [Action.Paper]
    }
    
    defeats=victories[user_action];
    print(type(victories))
    if(user_action==computer_action):
        print("Tied")
    elif(computer_action in defeats):
        print("user win")
    else:
        print("computer win")

while True:
    try:
        user_action=get_user_selection();
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action=computer_selection();
    determine_winner(user_action,computer_action);
    0
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

