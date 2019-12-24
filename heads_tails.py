import random

guess = input("heads or tails?: ").lower()
heads_tails_array = ['heads','tails']
flip = random.choice(heads_tails_array)

print(f"you guessed: {guess}")
print(f"coin flipped: {flip}")

if guess == flip:
    print("yay!")
else:
    print("oh no, guess again!")









