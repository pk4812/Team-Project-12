""" 
Names:      Sarah Adel, Richard Forng, Philemon Kim, Paul Sung
Assignment: Final Project
Due Date:   December 15th (8:00pm), 2022
INST326-ESG1 William S. Farmer Fall 2022
"""

import sys
import argparse
import pandas as pd

#creates a dataframe that takes in data from a .csv file and will give them headers.
df = pd.read_csv("contacts.csv", names = ["Names", "Emails", "Phone Numbers"])

def determine_favorites(favorites_input):
    """
    Comments:
        Takes input from user and creates a favorites contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """

    chosen_favorites = df.query('type.str.startswith(@favorites_input)', engine = "python")
    inquired_favorites = chosen_favorites.describe()
    print(inquired_favorites)

    pass

def determine_emer_con_list(emer_con_list_input):
    """
    Comments:
        Takes input from user and creates an emergency contact list group, using the dataframe.
    Parameters:
        
    Returns:
        
    """



    pass

def determine_work(work_input):
    """
    Comments:
        Takes input from user and creates a work contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def determine_education(education_input):
    """
    Comments:
        Takes input from user and creates an education contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def determine_hobbies(hobbies_input):
    """
    Comments:
        Takes input from user and creates a hobbies contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def determine_international(international_input):
    """
    Comments:
        Takes input from user and creates a international contacts group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def main(filename):
    """
    Comments:
        Will ask for certain inputs from user, as arguments, to create certain groups, using the dataframe.  
    Parameters:
        
    Returns:
        
    """
    favorites_input = input("Enter your Favorite contacts: ")
    emer_con_list_input = input("Enter your Emergency Contacts: ")
    work_input = input("Enter your Work related Contacts: ")
    education_input = input("Enter your School related Contacts: ")
    hobbies_input = input("Enter your Hobby Contacts: ")
    international_input = input("Enter your International Contacts: ")

    favorites = determine_favorites(favorites_input)
    emer_con_list = determine_emer_con_list(emer_con_list_input)
    work = determine_work(work_input)
    education = determine_education(education_input)
    hobbies = determine_hobbies(hobbies_input)
    international = determine_international(international_input)

    pass

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
    parser.add_argument('favorites', type = str, help = 'The names of the users favorite contacts')
    parser.add_argument('emergency', type = str, help = 'The names of the users emergency contacts')
    parser.add_argument('work', type = str, help = 'The name of the users work contacts')
    parser.add_argument('education', type = str, help = 'The name of the users school contacts')
    parser.add_argument('hobbies', type = str, help = 'The name of the users hobby contact')
    parser.add_argument('international', type = str, help = 'The name of the users international contacts')
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":

    args = parse_args(sys.argv[1:])

    main(args.main)