
import random
# pick word through user input or one of computer generated words
print("play with the computer or friend")

computer_generated_words = [
    'a','ability','able', 'about', 'above', 'accept', 'according', 'energy', 'management',
    'operation', 'opportunity', 'point', 'police', 'policy', 'political', 'politics', 'popular',
    'population', 'position', 'positive',

]
friend_input = input("is your friend going to type in their secret word?(y/n): ").lower()
friend_generated_answer = False

if friend_input == 'y':
    friend_generated_answer = True

if friend_generated_answer:
    secret_word = input('secret word: ')
else:
    secret_word = random.choice(computer_generated_words)


# secret_word = 'hello'
answer_spaces = []
array = []

# if letter is in word
# find index number of guess
count = 0
for x in secret_word:
    count = count + 1
    answer_spaces.append('___')
print(answer_spaces)

guess_count = 0


while '___' in answer_spaces:

    if guess_count < 7:
        guess_count = guess_count + 1
        guess = input("guess: ").lower()
        if guess in secret_word:
            for x in range(0, count):
                if guess == secret_word[x]:
                    answer_spaces[x] = guess
            print(answer_spaces)
        else:
            print("letter is not in the word")

        if guess == secret_word:
            for x in range(0, count):
                answer_spaces[x] = guess[x]
            print(answer_spaces)
            print("good job you guessed the word!!")
            break
    else:
        quit_game = input("REVEAL ANSWER??(y/n): ").lower()
        if quit_game == 'y':
            print(f"The answer was: {secret_word}")
            break
        else:
            guess_count = 0
else:
    print(secret_word)
    print("you got it right!")

