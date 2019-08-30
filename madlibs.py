#Mad Libs Project CS 1.1

#User Input
user_words = []

#
word_list = {
    "nouns" : ["Cat", "Dog", "Sheep", "Fish"],
    "verbs" : ["run", "jump", "kick", "scream", "drive", "drink", "fallen", "eaten"],
    "adj" : ["attractive", "chubby", "clean", "dirty", "silly", "thankful"],
    "conj": ["but", "and", "yet", "or", "because", "nor", "although", "since", "unless"]
}

#Gets user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

