import random

words = [ "profe braulio", "salma", "software", "valentines", "comida", "graduacion", "computadora", "abrigo", "casa",
          "otorrinolaringologo", "new horizons", "development", "successful", "arancel", "abracadabrante"
]

game_words = random.sample(words, 15)
mistakes = 0
total = len(game_words)
count = 1

print("Type the word shown and press Enter.\n")

for word in game_words:
    print("Word", count, "of", total, ":", word)
    user = input("Your input: ").strip()

    if user.lower() == "exit":
        print("\nGame stopped by user")
        break


    if user == word:
        print("Correct!\n")
    else:
        print("Incorrect!\n")
        mistakes += 1

    print("Mistakes so far:", mistakes)
    print()
    count += 1

played = count - 1

if played > 0:
    correct = played - mistakes
    accuracy = (correct / played) * 100

    print("Game finished")
    print("Correct:", correct)
    print("Incorrect:", mistakes)
    print("Accuracy:", round(accuracy, 2), "%")
else:
    print("No words completed.")

