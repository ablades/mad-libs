#Mad Libs Project CS 1.1
import random as r
import sys

story_list = []

story_type = ""

def set_story_type():
    global story_type 
    story_type = input("Enter in the type of story you would like:  \u001b[35m automatic"
    + "\x1b[0m or \u001b[35m manual \x1b[0m : ")

    #Randomly selects a word based on part of speech
def random_word(part_of_speech):
    word_list = {
        "nouns" : ["Cat", "Dog", "Sheep", "Fish"],
        "verbs" : ["running", "jumping", "kicking", "screaming", "driving", "drinking", "fallen", "eaten"],
        "adjs" : ["attractive", "chubby", "clean", "dirty", "silly", "thankful"],
        "names": ["Barry", "Gary", "Jerry", "Larry"]
    }

    return word_list[part_of_speech][r.randrange(len(word_list[part_of_speech]))]

#Gets and colors user input
def user_input(prompt, part_of_speech):
    if story_type == "manual":
        user_input = input(prompt)
    elif story_type == "automatic":
        user_input = random_word(part_of_speech)
    else:
        sys.exit("\u001b[31mInvalid Story Type. Please try again.  \x1b[0m")

    #Makes sure input is a string
    if not user_input.isalpha():
        sys.exit("\u001b[31mInput is not a string. Please try again.\x1b[0m")

    if part_of_speech == "nouns":
        user_input = "\u001b[31m" + user_input + "\x1b[0m" 
    elif part_of_speech == "verbs":
        user_input = "\u001b[32m" + user_input + "\x1b[0m"
    elif part_of_speech == "adjs":
        user_input = "\u001b[33m" + user_input + "\x1b[0m"
    elif part_of_speech == "names":
        user_input = "\u001b[34m" + user_input + "\x1b[0m"

    return user_input

#Prints out the completed story
def print_story():
    for line in story_list:
        print(line, end = '')

#Creates story from user input
def story_creation():
        set_story_type()
        story_list.append("Once upon a time there was a " + user_input(" Enter in a Noun: ", "nouns") + ".\n")
        story_list.append("That went by the name,")
        name = user_input(" Enter in a Name: ", "names")
        story_list.append(" " + name)
        story_list.append(".\n" + name + " was a ")
        story_list.append(user_input(" Enter an adjective: ", "adjs") + " thing ")
        story_list.append(user_input(" Enter a verb ending in ing: ", "verbs") + " late at night. \n")
        story_list.append(name + " was at a bar called " + user_input("Enter in a Noun(place): ", "nouns") + " and often stayed late. \n")
        story_list.append("One evening, on a " + user_input("Enter in an adjective: ", "adjs") + " and stormy night. \n")
        story_list.append("Lightning struck and knocked " + name + " into a cocktail of chemicals. \n")
        story_list.append("Once " + name + " awoke, they " + user_input("Enter in a verb(ing)","verbs") + " in agony and suddenly passed out. \n")
        story_list.append(name + " remained in a coma for 4 months. \n")
        story_list.append("Once " + name +" had woke he realized something had changed. \n")
        story_list.append("He was faster, stronger, quicker, and more " + user_input("Enter an adjective: ", "adjs") + ". \n")
        story_list.append("The journey for " + name + " was just beginning...   \n")
        print("\u001b[35m \nStory Creation Complete!! Here's your full story... \n \x1b[0m")
        print_story()

story_creation()