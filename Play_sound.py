# Play an audio file of the word to be spelled 
import os 
import sys
from playsound import playsound

#Sound function to play audio file of each word.
def sound(word):
     playsound(word)