import random

# pick index num 50 of a bunch of random possibilities for answer.
all_computer_generated_answer_possibilities = []
for x in range(1,101):
    random.shuffle(all_computer_generated_answer_possibilities)
    all_computer_generated_answer_possibilities.append(x)
answer = all_computer_generated_answer_possibilities[50]

# create array with numbers 1 through 100
all_possible_numbers = []
for x in range(1,101):
    all_possible_numbers.append(x)


print(f"guess the number between 1 and 100")
print("ask anything")
asked_question_numbers = []

# remove all numbers in array
# only add input numbers to array
# count number of numbers in array
# solve based on number of numbers in array
while asked_question_numbers != answer:

    for x in asked_question_numbers[:]:
        asked_question_numbers.pop()

    asked_question = input(f"question: ")
    amount_of_nums_in_question_asked = 0
    for x in asked_question.split():
        if x.isdigit():
            asked_question_numbers.append(x)
    for y in asked_question_numbers:
        amount_of_nums_in_question_asked += 1

    if amount_of_nums_in_question_asked == 2:
        if int(asked_question_numbers[0]) == answer or int(asked_question_numbers[1]) == answer:
            print(f"correct! the number WAS {answer}")
            break
        elif int(asked_question_numbers[0]) < answer < int(asked_question_numbers[1]) or (int(asked_question_numbers[0]) > answer > int(asked_question_numbers[1])):
            print("YES. number is between is between. ")
        else:
            print("no, number is not between")
    elif amount_of_nums_in_question_asked == 1:
        if int(asked_question_numbers[0]) != answer:
            print("that is not it :(")
        else:
            print("you got it!")
            break
    else:
        print("0/10 horrible question!")


