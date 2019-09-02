#Mad Libs Project CS 1.1
import random as r

story_list = []

story_type = ""

def set_story_type():

    global story_type 
    story_type = input("Enter in the type of story you would like:  \u001b[35m automatic"
    + "\x1b[0m or \u001b[35m manual \x1b[0m : ")


def random_word(part_of_speech):

    word_list = {
        "nouns" : ["Cat", "Dog", "Sheep", "Fish"],
        "verbs" : ["run", "jump", "kick", "scream", "drive", "drink", "fallen", "eaten"],
        "adjs" : ["attractive", "chubby", "clean", "dirty", "silly", "thankful"],
        "names": ["Barry", "Gary", "Jerry", "Larry"]
    }
    #Randomly selects a word based on part of speech
    return word_list[part_of_speech][r.randrange(len(word_list[part_of_speech]))]

#Gets and colors user input
def user_input(prompt, part_of_speech):

    if story_type == "manual":
        user_input = input(prompt)
    elif story_type == "automatic":
        user_input = random_word(part_of_speech)
    else:
        print("Invalid story type")
        return

    #Makes sure input is a string
    if not user_input.isalpha():
        print("Input is not a word")
        return

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
        print(line)



#Show line of story for user.
#Ask user for input
#Show next line ect
#At end show completed story with colors for each input
def story_creation():
        set_story_type()
        story_list.append(" Once upon a time there was a " + user_input(" Enter in a Noun: ", "nouns") + ".\n")
        story_list.append(" That went by the name, ")
        name = user_input(" Enter in a Name: ", "names")
        story_list.append(name)
        story_list.append(".\n" + name + " was a ")
        story_list.append(user_input(" Enter an adjective: ", "adjs"))
        story_list.append(user_input(" Enter a verb ending in ing: ", "verbs") + "away late at night. \n")
        story_list.append(name + "was at " + user_input("Enter in a Noun(place): ", "nouns") + " and often stayed late. \n")
        story_list.append("One evening on a " + user_input("Enter in an adjective: ", "adjs") + " stormy night. \n")
        story_list.append("Lightning struck and knocked barry into a cocktail of chemicals. \n")
        story_list.append("Barry remained in a coma for 4 months. \n")
        story_list.append("Once Barry had woke he realized something had changed. \n")
        story_list.append("He was faster, stronger, quicker, and more agile. \n")
        story_list.append("Barry would go on to be known as The Flash. \n")
        story_list.append("Story Creation Complete!! Here's your full story. \n")
        print_story()


story_creation()