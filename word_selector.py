# import necessary modules 
import os 
import sys
from Play_sound import sound 



def word_selector ():
    
    #Retreive a list of all the words in the files.
    list1_words = os.listdir('words/Level 1')
    list2_words = os.listdir('words/Level 2')
    list3_words = os.listdir('words/Level 3')
    list4_words = os.listdir('words/Level 4')

    #choice determines the level the user will spell at.
    choice = input("\tEnter the level you would like to spell at ")
    if choice == '1':
        words_list = list1_words
        location = 'words/Level 1/'
        total_marks = len(list1_words)
    elif choice == '2':
        words_list = list2_words
        location = 'words/Level 2/'
        total_marks = len(list2_words)
    elif choice =='3':
        words_list = list3_words
        location = 'words/Level 3/'
        total_marks = len(list3_words)
    elif choice == '4':
        words_list = list4_words     
        location = 'words/Level 4/' 
        total_marks = len(list4_words)
    else :
        choice = input("\tPlease enter a valid level  ")    

    mark = 0 
    #Loop through all the words in the level folder.
    for word in words_list:
        location = location + word
        #Play audio file of word
        sound(location)
        spelling_word = os.path.splitext(word)
        #while the answer is not right keep allowing the user to try spell the word correctly.
        right = False 
        while right == False:
            user_word = input("\t\tInput the spelling of the word: ").lower()
            if user_word == "answer":
                print("\t\tThe correct spelling is:",spelling_word[0]) 
                break
            elif user_word == spelling_word[0]:
                print("\t\tWell done !")  
                right = True 
                mark += 1 
                break
            else:
                print("\t\tThat's not it.Try again")
                sound(location)
               
        proceed = input("\t\tWould you like to continue?y/n?").lower() 
        if proceed == "n":
            print("\t\tYou got a total mark of ",mark," out of a potential ",total_marks) 
            return        
        #Remove current word from word path to allow another word to take its place.        
        location = location.strip(word)    
    print("\t\tYou got a total mark of ",mark," out of ",total_marks)    

    





 





