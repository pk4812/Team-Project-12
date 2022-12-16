""" 
Names:      Sarah Adel, Richard Forng, Philemon Kim, Paul Sung
Assignment: Final Project
Due Date:   December 16th (11:59pm), 2022
INST326-ESG1 William S. Farmer Fall 2022
"""

import sys
import argparse
import pandas as pd

def contacts_picker(input, df):
    """Takes contact name input from user and creates a filtered contact group 
    using the dataframe. Returns filtered group for that category.
    
    Arguments:
        input (tuple): collection of names the user wants to put in a category
        df (dataframe): pandas dataframe of the contacts list csv
    Returns:
        chosen_contacts (dataframe): filtered dataframe group filtered by name
    """
    chosen_contacts = df.query('Names.str.startswith(@input)', engine = "python")
    return(chosen_contacts)

def print_menu():
    """Outputs menu options to terminal for user interface
    
    Arguments:
        None
    Returns:
        None
    """
    print(
    """
    -------------------------------------------
    \t\tCREATING CONTACTS LIST
    -------------------------------------------
    Please choose one of the following options:
    1. Create a Favorites Group
    2. Create a Emergency Contacts Group
    3. Create a Work Group
    4. Create a Education Group
    5. Create a Hobbies Group
    6. Create a International Group
    7. Exit Program
    """
    )

def choice():
    """Asks for user's choice within the menu options
    
    Arguments:
        None
    Returns:
        choice (int): the numbered menu option for operation
    """
    choice = int(input("\nPlease enter your choice: "))
    return choice

def contacts(filename:str):
    """Method that prints out the .csv file after the menu to show their contact options.
    
    Arguments:
        Filename.
    Returns:
        Printed csv file in dataframe format.
    """
    df = pd.read_csv(filename, names = ["Names", "Emails", "Phone Numbers"])
    print("Here are your contacts list to choose from: \n", df)

def main(filename:str):
    """Will receive certain inputs from user, as arguments, to create filtered groups, using the dataframe.  
    
    Arguments:
        Filename.
    Returns:
        Users filtered contacts list. 
    """
    #Calls the printed menu function
    print_menu()

    #Calls the printed contacts list
    contacts(filename)

    #Creates a dataframe that takes in data from a .csv file and will give them headers.
    df = pd.read_csv(filename, names = ["Names", "Emails", "Phone Numbers"])

    #Receives inputs from the command line
    menu_choice = 1
    methods_ran = []

    while menu_choice in (1, 2, 3, 4, 5, 6, 7):
        menu_choice = choice()
        if menu_choice == 1:
            favorites_input = tuple(input("Enter your Favorite Contacts Name(s): ").split(", "))
            favorites = contacts_picker(favorites_input, df)
            methods_ran.append(1)

        elif menu_choice == 2:
            emer_con_list_input = tuple(input("Enter your Emergency Contacts Name(s): ").split(", "))
            emer_con_list = contacts_picker(emer_con_list_input, df)
            methods_ran.append(2)

        elif menu_choice == 3:
            work_input = tuple(input("Enter your Work related Contacts Name(s): ").split(", "))
            work = contacts_picker(work_input, df)
            methods_ran.append(3)

        elif menu_choice == 4:
            education_input = tuple(input("Enter your School related Contacts Name(s): ").split(", "))
            education = contacts_picker(education_input, df)
            methods_ran.append(4)

        elif menu_choice == 5:
            hobbies_input = tuple(input("Enter your Hobby Contacts Name(s): ").split(", "))
            hobbies = contacts_picker(hobbies_input, df)
            methods_ran.append(5)

        elif menu_choice == 6:
            international_input = tuple(input("Enter your International Contacts Name(s): ").split(", "))
            international = contacts_picker(international_input, df)
            methods_ran.append(6)

        elif menu_choice == 7:
            
            methods_ran.append(7)
            methods_ran.sort()

            for method in methods_ran:
                if method == 1:
                    print("\nHere are your Favorites Contact(s): \n", favorites)
                elif method == 2:
                    print("\nHere are your Emergency Contacts Contact(s): \n", emer_con_list)
                elif method == 3:
                    print("\nHere are your Work Contact(s): \n", work)
                elif method == 4:
                    print("\nHere are your Education Contact(s): \n", education)
                elif method == 5:
                    print("\nHere are your Hobbies Contact(s): \n", hobbies)
                elif method == 6:
                    print("\nHere are your International Contact(s): \n", international)
                elif method == 7:
                    sys.exit("\nGoodbye.")

        else:
            print("\nInvalid input, Please enter a choice between 1-7: ")
            menu_choice = choice()

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Arguments:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'The name of the file wth the contact data')
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":
    """_summary_
    """
    args = parse_args(sys.argv[1:])
    main(args.filename)