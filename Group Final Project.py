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
df = pd.read_csv()

def favorites():
    """
    Comments:
        Takes input from user and creates a favorites contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    pass

def emer_con_list():
    """
    Comments:
        Takes input from user and creates an emergency contact list group, using the dataframe.
    Parameters:
        
    Returns:
        
    """



    pass

def work():
    """
    Comments:
        Takes input from user and creates a work contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def education():
    """
    Comments:
        Takes input from user and creates an education contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def hobbies():
    """
    Comments:
        Takes input from user and creates a hobbies contact group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def international():
    """
    Comments:
        Takes input from user and creates a international contacts group, using the dataframe.
    Parameters:
        
    Returns:
        
    """


    
    pass

def main():
    """
    Comments:
        Will ask for certain inputs from user, as arguments, to create certain groups, using the dataframe.  
    Parameters:
        
    Returns:
        
    """


    
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
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE FAVORITES GROUP WILL BE ADDED.
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE EMERGENCY CONTACT LIST GROUP WILL BE ADDED.
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE WORK GROUP WILL BE ADDED.
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE EDUCATION GROUP WILL BE ADDED.
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE HOBBIES GROUP WILL BE ADDED.
        #ARGUMENT THAT TAKES IN INPUT FROM USER TO CREATE INTERNATIONAL GROUP WILL BE ADDED.
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":

    args = parse_args(sys.argv[1:])

    main(args.main)