weight = input("what is your weight?: ")
unit = input("(L)bs or (K)gs?: ")





lb = False
kg = False

if unit == 'l' or unit == 'L':
    lb = True
elif unit == 'k' or unit == 'K':
    kg = True
else:
    print("type in a l or k")

if lb:
    print(int(weight)*.45)
if kg:
    print(int(weight)*2.2)


if unit.upper() == "L":
    converted =