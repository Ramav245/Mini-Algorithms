

def addcustomer(name):
    all_names.append(name)
    ask_age = int(input("What is your age?: "))
    all_ages.append(ask_age)
    ask_membership = input("Do you want to be a member?: ")
    all_membership_information.append(ask_membership)
    print(f"Name: {name}")
    print(f"Age: {ask_age}")
    print(f"Membership: {ask_membership}")
    print(f"Info saved, Thank you")


all_names = ['john','eric','tom','smith']
all_ages = [25,34,34,10]
all_membership_information = ['yes','no','no','yes']

customer_request = input('Requested Name: ').lower()

if customer_request not in all_names:
    print("NOT IN DATABASE")
    add = input("want to add?(yes/no): ").lower()
    if add == 'yes':
        addcustomer(customer_request)
    else:
        print("ok bye")
else:
    print("IN DATABASE")
    index_number = all_names.index(customer_request)

    customer_information = {
        'Name': all_names[index_number],
        'Age': all_ages[index_number],
        'Member': all_membership_information[index_number]
    }

    print(f"Name: {customer_information.get('Name')}")
    print(f"Age: {customer_information.get('Age')}")
    print(f"Membership: {customer_information.get('Member')}")



