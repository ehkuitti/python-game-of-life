INSTRUCTIONS = "instructions.txt"
CREDITS = "credits.txt"


def open_file(file_name):

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
    instructions_file = open_file(INSTRUCTIONS)
    if instructions_file is not None:
        print_file_contents(instructions_file)

    credits_file = open_file(CREDITS)


def print_welcome_message():

def ask_player_name():

    # Booleans
    is_player_name_valid = False

    while not is_player_name_valid:
        player_name = input("What's your name?")
        if player_name == "":
            print("Please input a valid name!")

        else:
            print_welcome_message()



def main():

    # VARIABLE INITIALIZATIONS BY VARIABLE TYPE

    # Booleans
    is_place_of_birth_valid = False

    # Integers
    switch_operator = int(0)

    # Strings
    player_name = ""
    player_place_of_birth = ""

    parse_required_text_files()
    player_name = ask_player_name()


if __name__ == "__main__":
    main()
