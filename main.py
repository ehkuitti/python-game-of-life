def open_instructions():

    # Strings
    filename = "instructions.txt"

    while True:
        try:
            instruction_file = open(filename, mode="r")
            break

        except IOError:
            print("Please check that the instructions file is placed in the "
                  "same folder with the program.")
            print("Press enter to try again.")

    for line in instruction_file:
        print(line)

    return instruction_file


def main():

    # VARIABLE INITIALIZATIONS BY VARIABLE TYPE

    # Booleans
    is_place_of_birth_valid = False

    # Integers
    switch_operator = int(0)

    # Strings
    player_name = ""
    player_place_of_birth = ""

    file = open_instructions()


if __name__ == "__main__":
    main()
