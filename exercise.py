numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if (number%2) == 0:
            evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    if choice == "q":
        return "Quit"

def who_do_you_know():
    people_list = input("List the names of people you know? ")
    split_list = people_list.split()
    return split_list

def ask_user():
    user_input = input("Give us a name please? ")
    friend_list = who_do_you_know()
    for name in friend_list:
        if name == "user_input":
            print "you know the name"
        else:
            print "sorry you don't know the person"

