""" 
Names:      Sarah Adel, Richard Forng, Philemon Kim, Paul Sung
Assignment: Final Project
Due Date:   December 15th (8:00pm), 2022
INST326-ESG1 William S. Farmer Fall 2022
"""

import sys
import argparse
import pandas as pd



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