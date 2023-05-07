from random import randrange

INSTRUCTIONS = "instructions.txt"
CREDITS = "credits.txt"


class Player:
    def __init__(self, name="", age=0, place_of_birth=""):
        self.__name = name
        self.__age = age
        self.__place_of_birth = place_of_birth

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_place_of_birth(self):
        return self.__place_of_birth

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_place_of_birth(self, place_of_birth):
        self.__place_of_birth = place_of_birth


def open_a_file(file_name):

    while True:
        try:
            text_file = open(file_name, mode="r")
            break

        except IOError:
            print(f"Please make sure that the text file {file_name} is placed "
                  f"in the the same folder with the program "
                  "and then run the game again.")
            return None

    return text_file


def print_file_contents(text_file):

    for line in text_file:
        print(line)


def parse_required_text_files():
    instructions_file = open_a_file(INSTRUCTIONS)
    if instructions_file is not None:
        print_file_contents(instructions_file)
        instructions_file.close()

    credits_file = open_a_file(CREDITS)
    credits_file.close()


def generate_random_value(desired_high_limit=10):
    """This function generates a random value below the desired high limit
    and then returns it to the caller. The randrange function is imported
    from the random built-in library. The default range is 0-9."""

    return randrange(desired_high_limit)


def print_welcome_message(player_name):

    amount_of_options = 11

    random_value = generate_random_value(amount_of_options)

    if random_value == 0:
        print(f"I love the name {player_name}!")
    elif random_value == 1:
        print(f"{player_name} is a nice name!")
    elif random_value == 2:
        print(f"{player_name} is the nicest name I have ever heard!")
    elif random_value == 3:
        print(f"{player_name} is a fine name if you ask me!")
    elif random_value == 4:
        print(f"{player_name} has to be the coolest name in existence!")
    elif random_value == 5:
        print(f"{player_name}, I've never heard of your name!")
    elif random_value == 6:
        print(f"Wow, is it really {player_name} playing this game? I'm honored")
    elif random_value == 7:
        print(f"Wow, it's the {player_name}!")
    elif random_value == 8:
        print(f"I never knw you liked this game, {player_name}")
    elif random_value == 9: 
        print(f"It's really you, {player_name}. Wow!")
    elif random_value == 10:
        print(f"You can't imagine how lucky you, {player_name}, are playing "
              f"this rare gem!")


def is_input_empty(my_input):
    """The function stripts the input of whitespaces. If the result of this
    operation is an empty string, then the player didn't input anything.
    Returns a boolean value based on the result."""

    if my_input.strip() == "":
        return True

    return False


def ask_player_name():

    # VARIABLE INITIALIZATIONS ORDERED BY TYPE ALPHABETICALLY

    # Booleans
    is_player_name_valid = False
    
    # Strings
    player_name = ""

    while not is_player_name_valid:
        player_name = input("What's your name? ")
        if is_input_empty(player_name):
            print("Please input a valid name!")
        else:
            print_welcome_message(player_name)
            is_player_name_valid = True
            
    return player_name


def is_input_inside_range(my_number, low_limit, high_limit):
    """Function checks whether a number is withing a desired range and
    returns a boolean based on the answer. The variable my_number is
    converted into an integer to avoid type errors. Returns a false if the
    conversion fails."""

    try:
        if low_limit < int(my_number) < high_limit:
            return True
    except TypeError:
        return False
    except ValueError:
        return False

    return False


def ask_place_of_birth():

    # VARIABLE INITIALIZATIONS ORDERED BY TYPE ALPHABETICALLY

    # Booleans
    is_place_of_birth_valid = False

    # Integers, cities
    helsinki = 1
    tampere = 2
    turku = 3

    # Integers, miscellaneous
    place_of_birth_selection = 0

    # Strings
    place_of_birth = ""

    print()
    print("Select your place of birth:")
    print("1: Helsinki")
    print("2: Tampere")
    print("3: Turku")

    while not is_place_of_birth_valid:
        place_of_birth_selection = input()

        if is_input_empty(place_of_birth_selection):
            print("Please input a number!")

        elif not is_input_inside_range(place_of_birth_selection, 1, 4):
            print("Please input a number within range 1-3!")

        else:

            if place_of_birth_selection == helsinki:
                place_of_birth = "Helsinki"
                is_place_of_birth_valid = True

            elif place_of_birth_selection == tampere:
                place_of_birth = "Tampere"
                is_place_of_birth_valid = True

            else:
                place_of_birth = "Turku"
                is_place_of_birth_valid = True

    return place_of_birth


def print_credits():
    credits_file = open_a_file("credits.txt")
    print_file_contents(credits_file)
    

def life_path_turku():
    print("Who would want to be born in Turku...")
    print_credits()


def life_path_not_turku():
    """TO BE IMPLEMENTED. The game continues if the player chooses not to be
    born in Turku, i.e. not to die immediately."""


def life_path_according_to_place_of_birth(place_of_birth):

    if place_of_birth == "Helsinki":
        life_path_not_turku()
    elif place_of_birth == "Tampere":
        life_path_not_turku()
    else:
        life_path_turku()
        return None


def main():

    # VARIABLE INITIALIZATIONS BY VARIABLE TYPE

    # Booleans
    is_place_of_birth_valid = False

    player = Player()

    parse_required_text_files()

    # Asking information from the player
    player.set_name(ask_player_name())
    player.set_place_of_birth(ask_place_of_birth())

    if life_path_according_to_place_of_birth(player.get_place_of_birth()) \
            is None:
        return


if __name__ == "__main__":
    main()
