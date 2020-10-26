
word_to_find = []
game_state = []
old_guesses = []
user_guess = ""
pos = 0
i = 0
remain_try = 6

def you_win():
    print("Félicitation ! Le mot à trouver était " + user_input)

def convert_to_array(string):
    word_to_find[:0]=user_input
    return word_to_find

def give_game_state(word_to_find):
    for letters in word_to_find:
        if letters == " ":
            game_state.append(" ")
        else:
            game_state.append("_")
    return ''.join(game_state)

def give_letter_pos(letter):
    pos = word_to_find.index(letter)
    word_to_find[pos] = 0
    game_state[pos] = letter

user_input = input("Entrez le mot à deviner: ")
print("\n" * 100)
convert_to_array(user_input)
give_game_state(word_to_find)
print(' '.join(game_state))

while True:
    duplicate_letter = False
    user_guess = input("Entrez une lettre ou le mot à trouver: ")
    for letter_stored in old_guesses:
        if letter_stored == user_guess:
            print("Vous avez déjà essayé cette lettre !")
            print(' '.join(game_state))
    if user_guess not in old_guesses:
        old_guesses.append(user_guess)
        duplicate_letter = True

    for letter in word_to_find:
        if letter == user_guess:
            give_letter_pos(letter)
            i += 1
            if letter not in word_to_find:
                print(' '.join(game_state))
    if user_guess not in user_input and duplicate_letter == True:
        remain_try -= 1
        print(user_guess + " n'est pas dans le mot !" )
        print("Il vous reste " + str(remain_try) + " essais")
        print(' '.join(game_state))
        if remain_try == 0:
            print("Vous avez perdu ! Le mot à trouver était " + user_input)
            break

    if i == len(word_to_find):
        you_win()
        break

    if user_guess == user_input:
        you_win()
        break

