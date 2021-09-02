##### Taş Kağıt Makas Oyunu #####

import random
import time

finish_count = int(input("How many games you want as finish point? "))

print("""\nTo select the elements please type;
          s for Scissors
          r for Rock
          p for Paper\n
      """)
      
      
player_wins = 0
computer_wins = 0

def player_select():
    p_select = input("Scissors, Rock or Paper? ")
    p_select = p_select.lower()
    if p_select not in ["s", "r", "p"]:
        print("\nWrong selection has been made. Could you please type your selection again?\n")
        player_select()
    return p_select

def computer_select():
    c_select = random.randint(0,2)
    if c_select == 0:
        c_select = "s"
    elif c_select == 1:
        c_select = "r"
    elif c_select == 2:
        c_select = "p"
    return c_select
        
while True:
    p_select = player_select()
    c_select = computer_select()
    
    if p_select == "s":
        if c_select == "s":
            print("You have selected Scissors and computer selected Scissors. No one wins.\n")
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "p":
            print("\nYou have selected Scissors and computer selected Paper. You win!\n")
            player_wins = player_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "r":
            print("You have selected Scissors and computer selected Rock. Computer wins!\n")
            computer_wins = computer_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
    elif p_select == "r":
        if c_select == "r":
            print("You have selected Rock and computer selected Rock. No one wins.\n")
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "s":
            print("\nYou have selected Rock and computer selected Scissors. You win!\n")
            player_wins = player_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "p":
            print("You have selected Rock and computer selected Paper. Computer wins!\n")
            computer_wins = computer_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
    else:
        if c_select == "s":
            print("You have selected Paper and computer selected Scissors. Computer wins!\n")
            computer_wins = computer_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "r":
            print("\nYou have selected Paper and computer selected Rock. You win!\n")
            player_wins = player_wins + 1
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
        elif c_select == "p":
            print("You have selected Paper and computer selected Paper. No one wins.\n")
            print("Player: " + str(player_wins) + " Computer: " + str(computer_wins))
            
    if player_wins == finish_count or computer_wins == finish_count:
        if player_wins > computer_wins:
            print("You won! Congratss!!")
            print("Program will be closed automatically in 10 seconds, if you have guts, come back!")
            time.sleep(10)
        else:
            print("Computer won! You are a looser!")
            print("Program will be closed automatically in 10 seconds. If you are still there, come back and save your pride... LOOSER")
            time.sleep(10)
        break
            

