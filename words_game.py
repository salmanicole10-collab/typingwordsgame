import random

words = [
    "apple","banana","orange","grape","peach",
    "chair","table","window","pencil","notebook",
    "ocean","mountain","river","forest","desert",
    "python","github","commit","branch","merge"
]

game_words = random.sample(words, 15)
print(game_words) 
