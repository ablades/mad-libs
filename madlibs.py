#Mad Libs Project CS 1.1

#User Input
user_words = []

story_list = []

#
word_list = {
    "nouns" : ["Cat", "Dog", "Sheep", "Fish"],
    "verbs" : ["run", "jump", "kick", "scream", "drive", "drink", "fallen", "eaten"],
    "adj" : ["attractive", "chubby", "clean", "dirty", "silly", "thankful"],
    "conj": ["but", "and", "yet", "or", "because", "nor", "although", "since", "unless"]
}

#Gets and colors user input
def user_input(prompt, part_of_speech):

    user_input = input(prompt)

    if(part_of_speech == "noun"):
        user_input = "\u001b[31m" + user_input + "\x1b[0m"
    elif(part_of_speech == "verb"):
        user_input = "\u001b[32m" + user_input + "\x1b[0m"
    elif(part_of_speech == "adj"):
        user_input = "\u001b[33m" + user_input + "\x1b[0m"
    elif(part_of_speech == "conj"):
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
    story_list.insert(0, "Once upon a time there was a ")
    story_list.insert(1, user_input("Enter in a Noun or Name of Character", "Noun") + ".\n")
    "Named was Barry Allen. \n"
    "Barry was a hard working man and often stayed late for work. \n"
    "One evening on a dark stormy night as Barry finished work. \n"
    "Lightning struck and knocked barry into a cocktail of chemicals. \n"
    "Barry remained in a coma for 4 months. \n"
    "Once Barry had woke he realized something had changed. \n"
    "He was faster, stronger, quicker, and more agile. \n"
    "Barry would go on to be known as The Flash. \n"


