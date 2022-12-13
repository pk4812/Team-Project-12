""" 
Names:      Sarah Adel, Richard Forng, Philemon Kim, Paul Sung
Assignment: Final Project
Due Date:   December 15th (8:00pm), 2022
INST326-ESG1 William S. Farmer Fall 2022
"""

import sys
import argparse
import pandas as pd

def contacts_picker(input, df):
    """
    Comments:
        Takes input from user and creates a favorites contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """
    
    chosen_contacts = df.query('Names.str.startswith(@input)', engine = "python")

    return(chosen_contacts)

def print_menu():

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
    7. Exit Program"""
    )

def choice():
    
    choice = int(input("\nPlease enter your choice: "))

    return choice

def main(filename:str):
    """
    Comments:
        Will ask for certain inputs from user, as arguments, to create certain groups, using the dataframe.  
    Parameters:
        
    Returns:
        
    """

    #creates a dataframe that takes in data from a .csv file and will give them headers.
    df = pd.read_csv(filename, names = ["Names", "Emails", "Phone Numbers"])

    #Calls the printed menu function
    print_menu()

    #Receives inputs from the command line
    menu_choice = 1
    methods_ran = []
    while menu_choice in (1, 2, 3, 4, 5, 6, 7):
        menu_choice = choice()
        if menu_choice == 1:
            favorites_input = tuple(input("Enter your Favorite contacts: ").split(", "))
            favorites = contacts_picker(favorites_input, df)
            methods_ran.append(1)

        elif menu_choice == 2:
            emer_con_list_input = tuple(input("Enter your Emergency Contacts: ").split(", "))
            emer_con_list = contacts_picker(emer_con_list_input, df)
            methods_ran.append(2)

        elif menu_choice == 3:
            work_input = tuple(input("Enter your Work related Contacts: ").split(", "))
            work = contacts_picker(work_input, df)
            methods_ran.append(3)

        elif menu_choice == 4:
            education_input = tuple(input("Enter your School related Contacts: ").split(", "))
            education = contacts_picker(education_input, df)
            methods_ran.append(4)

        elif menu_choice == 5:
            hobbies_input = tuple(input("Enter your Hobby Contacts: ").split(", "))
            hobbies = contacts_picker(hobbies_input, df)
            methods_ran.append(5)

        elif menu_choice == 6:
            international_input = tuple(input("Enter your International Contacts: ").split(", "))
            international = contacts_picker(international_input, df)
            methods_ran.append(6)

        elif menu_choice == 7:

            methods_ran.append(7)
            methods_ran.sort()

            for method in methods_ran:
                if method == 1:
                    print("\nHere are your Favorites Contacts: \n", favorites)
                elif method == 2:
                    print("\nHere are your Emergency Contacts Contacts: \n", emer_con_list)
                elif method == 3:
                    print("\nHere are your Work Contacts: \n", work)
                elif method == 4:
                    print("\nHere are your Education Contacts: \n", education)
                elif method == 5:
                    print("\nHere are your Hobbies Contacts: \n", hobbies)
                elif method == 6:
                    print("\nHere are your International Contacts: \n", international)
                elif method == 7:
                    sys.exit("\nGoodbye.")

def parse_args(args_list):
    """
    Comments:
        Takes a list of strings from the command prompt and passes them through as arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type = str, help = 'The name of the file wth the contact data')
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":

    args = parse_args(sys.argv[1:])

    main(args.filename)