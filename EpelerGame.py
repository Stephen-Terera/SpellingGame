from welcome_message import welcome_message
from word_selector import word_selector
import sys
import os 

def main():
    welcome_message()   
    word_selector()
    print("\t\tThank you for playing")

#Loop to keep the game going.
while True:
    main()