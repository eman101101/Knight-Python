# Call this function to create a new knight

def create_knight(knights):
    # Create a dictionary for the knight
    knight_data = {}

    print("Let's create a knight!")

    # Set up information for the knight using input from user
    name = str(input("What is the knight's name? "))
    armour_colour = str(input("What is the knights armour colour? "))
    while True:
        try:
            age = int(input("What is the knight's age? "))
            break
        except ValueError:
            print("Please enter a valid integer for age.")
    while True:
        try:
            power_level = int(input("What is the knights power level? "))
            break
        except ValueError:
            print("Please enter a valid integer for power level.")
            
    # Add information to dictionary
    knight_data['name'] = name
    knight_data['age'] = age
    knight_data['armour_colour'] = armour_colour
    knight_data['power_level'] = power_level

    # Add dictionary to list of knights
    knights.append(knight_data)

# Call this function to update a knights info

def update_knight(knights):
    # Check if there are no knights in the list
    if not knights:
        print("No knights available for update. Please create a knight first.")
        return

    # Display available knights for update
    print("Select a knight to update:")
    for index, knight in enumerate(knights):
        print(f"{index + 1}: {knight['name']}")

    # Get user input for knight selection
    knight_index = int(input("Enter the knight number: ")) - 1

    # Validate knight selection
    if knight_index < 0 or knight_index >= len(knights):
        print("Invalid knight number.")
        return

    # Select the knight for update
    selected_knight = knights[knight_index]

    print(f"Updating {selected_knight['name']}")

    # Get user input for new knight details
    name = str(input("What is the knight's name? "))
    armour_colour = str(input("What is the knight's new armour colour? "))
    while True:
        try:
            age = int(input("What is the knight's age? "))
            break
        except ValueError:
            print("Please enter a valid integer for age.")
    while True:
        try:
            power_level = int(input("What is the knights power level? "))
            break
        except ValueError:
            print("Please enter a valid integer for power level.")

    # Update the selected knight's information
    selected_knight['name'] = name
    selected_knight['age'] = age
    selected_knight['armour_colour'] = armour_colour
    selected_knight['power_level'] = power_level

# Call this function to have your knights battle based on power level

def battle_knights(knights):
    print("This will show your knight with the highest power level!\n")
    if len(knights) < 2:
        print("Not enough knights to battle! Create at least two knights.\n")
        return
    
    # Find the knight with the highest power level using the max function and a lambda function
    winner = max(knights, key=lambda x: x['power_level'])
    print(
        f"The winner is {winner['name']} with a power level of {winner['power_level']}!\n")

# This is the menu and we make our selections here

def menu(knights_number):

    # Print the display options
    print("---Welcome to Evan's Knight Battleground!---\n")
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: Battle the knights!")
    print("0: Exit")

    try:
        # Take the users selction option
        select = int(input("Selection number: "))
        print()  # Creates a blank line

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            # Print out the Knights that were made
            for index, knight in enumerate(knights):
                print(
                    f"\nKnight {index+1}:\nName: {knight['name']} \nAge: {knight['age']} \nArmour Colour: {knight['armour_colour']} \nPower Level: {knight['power_level']}")
            knights_number += 1
            menu(knights_number)
        elif select == 2:
            update_knight(knights)

            # Print out the updated Knight's list
            for index, knight in enumerate(knights):
                print(
                    f"\nKnight {index+1}:\nName: {knight['name']} \nAge: {knight['age']} \nArmour Colour: {knight['armour_colour']} \nPower Level: {knight['power_level']}")
            menu(knights_number)

        elif select == 3:
            battle_knights(knights)
            menu(knights_number)

        elif select == 0:
            print("--- All your Knights! ---")

            # Print out the Knights that were made
            for index, knight in enumerate(knights):
                print(
                    f"\nKnight {index+1}:\nName: {knight['name']} \nAge: {knight['age']} \nArmour Colour: {knight['armour_colour']} \nPower Level: {knight['power_level']}")

        # Making sure an integer is entered
        else:
            print("--- Enter a number peasent! ---\n")
            menu(knights_number)

    # Making sure an integer is entered
    except:
        print("--- Enter a number peasent! ---\n")
        menu(knights_number)

knights_number = 0
knights = []

menu(knights_number)
