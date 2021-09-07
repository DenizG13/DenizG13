# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:58:16 2021

@author: deniz
"""
import random
import string
import support as sp
import time


data_all = sp.words

def letter_select(data_all):
    word = random.choice(data_all)
    if " " in word or "-" in word:
        word = random.choice(sp.words)
        letter_select()
    return word.upper()

def hangman():
    word = letter_select(data_all)
    word_letters = set(word)
    letters_all = set(string.ascii_uppercase)
    used_letters = set()
    end_game = 7
    
    while len(word_letters) > 0 and end_game > 0:
        print(f"Cemil has {end_game} lives before you kill him or save him from the death.")
        print("You have used these characters until now; "," ".join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        if end_game == 7:
            print("")
            print("Current Word", " ".join(word_list))
        elif end_game == 6:
            print(sp.fault_1)
            print("Current Word", " ".join(word_list))
        elif end_game == 5:
            print(sp.fault_2)
            print("Current Word", " ".join(word_list))
        elif end_game == 4:
            print(sp.fault_3)
            print("Current Word", " ".join(word_list))
        elif end_game == 3:
            print(sp.fault_4)
            print("Current Word", " ".join(word_list))
        elif end_game == 2:
            print(sp.fault_5)
            print("Current Word", " ".join(word_list))
        elif end_game == 1:
            print(sp.fault_6)
            print("Current Word", " ".join(word_list))
        
            
        user_letter = input("Guess a character: ").upper()
        print("""
              
              
              """)
        if user_letter in letters_all - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("\n")
                
            else:
                end_game = end_game - 1
                
        elif user_letter in used_letters:
            print("You have already tried it, please try again.")
            
        else:
            print("This is not valid.")
            
        
    if end_game == 0:
        print(sp.fault_7)
        print("Sorry you could not find the word. Cemil has died because of you LOOSER!\n")
        print(f"The word was {word}!")
        print("\nProgram will be closed automatically in 15 seconds. Cemil is died, Iffet is crying.")
        time.sleep(15)
        
    else:
        print(sp.free)
        print(f"YAYY you find the word {word} Cemil is free to go!")
        print("\nProgram will be closed automatically in 15 secons. Cemil and Iffet will go to picnic.")
        time.sleep(15)
        
if __name__ == '__main__':
    hangman()
     
