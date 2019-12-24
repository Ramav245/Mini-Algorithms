import random
name1 = input("name1: ")
name2 = input("name2: ")
name3 = input("name3: ")
name4 = input("name4: ")

names = [name1, name2, name3, name4]
names.sort()

n1,n2,n3,n4 = names

"used to find the total number of (names)variations for four people"
total_number_of_variations_of_people_in_line = 1
spots_in_line = 4
if spots_in_line == 4:
    for x in range(1,spots_in_line+1):
        total_number_of_variations_of_people_in_line *= x
    "print(total_number_of_variations_of_people_in_line)"

"go through all 24 variations of the 4 people standing in order and print one random order"
for y in range(1, total_number_of_variations_of_people_in_line+1):
    random.shuffle(names)

new_name1,new_name2,new_name3,new_name4 = names
"""
"shuffle all 100 values and put them into array to pick 4 random ages"
ages = []
for x in range(1,100):
    random.shuffle(ages)
    ages.append(x)
"print(ages)"

"find all random four peoples ages and put them into an array"
first_four_ages = []
for x in range(0,4):
    x_person_age = random.choice(ages)
    first_four_ages.append(x_person_age)

"new order and ages of the game"
new_age1,new_age2,new_age3,new_age4 = first_four_ages


"THIS IS THE ANSWER OF THE CORRECT ORDER OF AGES"
print(first_four_ages)

"FIRST FOUR AGES ARE SORTED TO BE ABLE SET HINTS AND MOVE NEW_AGE VARIABLES EFFECTIVELY"
first_four_ages.sort()

print(f"possible ages of {names}: {first_four_ages} ")

print(new_age1)
print(new_age2)
print(new_age3)
print(new_age4)

"Helpful Hints for person AGES before the start of the game"
Hint6 = "Hint6: oldest person will always stand in the back"
Hint7 = "Hint7: consecutive two spots in the center will never stand by each other"
Hint8 = "Hint8: first person in like never likes to stand next to someone older next to him"

"""
print(names)
"Helpful Hints for person PLACES before the start of the game"
Hint1 = f"Hint1: {new_name1} does not like standing in the back of the line"
Hint2 = f"Hint2: {new_name2} stands in spot 2"
Hint3 = f"Hint3: {new_name3} does not like standing in the front of the line"
Hint4 = f"Hint4: {new_name4} don't like standing in either of the center spots"
Hint5 = f"Hint5: {new_name1} hates {new_name3}"
print(Hint1)
print(Hint2)
print(Hint3)
print(Hint4)
print(Hint5)


print("FIND THE ORDER OF THE FOUR PEOPLE IN LINE!!")
"ask user for the answers of that they want to guess and answer CORRECT if correct"
answers = 0

input_name1 = input("Name of first person in line?: ")
if input_name1 == new_name1:
    print("CORRECT")
    answers += 1
else:
    print("INCORRECT")

input_name2 = input("Name of second person in line?: ")
if input_name2 == new_name2:
    print("CORRECT")
    answers += 1
else:
    print("INCORRECT")

input_name3 = input("Name of third person in line?: ")
if input_name3 == new_name3:
    print("CORRECT")
    answers += 1
else:
    print("INCORRECT")

input_name4 = input("Name of fourth person in line?: ")
if input_name4 == new_name4:
    print("CORRECT")
    answers += 1
else:
    print("INCORRECT")

print(f"you got {answers} correct")
print(f"the correct answer {names}")




















