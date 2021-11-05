"""
Utility function(s) for use in advent of code 2021

Alexander Griffen, 2021
"""
import os
import re
import __main__

def get_input():
    """ Returns a list, where each element is a string containing one
    line of the input file"""
    path = os.path.dirname(__main__.__file__)
    name = os.path.basename(__main__.__file__)
    if not re.fullmatch('.+_\d{1,2}\.py', name):
        raise RuntimeError('Invalid script name.')
    day = name.split('_')[-1].split('.')[0]
    try:
        with open(path+'/../inputs/' + day + '.txt', 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        raise RuntimeError('No input file found for this day.')
    return [x.strip() for x in content]

def get_test():
    """ Returns a list, where each element is a string containing one
    line of the testing file"""
    path = os.path.dirname(__main__.__file__)
    name = os.path.basename(__main__.__file__)
    if not re.fullmatch('.+_\d{1,2}\.py', name):
        raise RuntimeError('Invalid script name.')
    day = name.split('_')[-1].split('.')[0]
    try:
        with open(path+'/../test_inputs/' + day + '.txt', 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        raise RuntimeError('No test input file found for this day.')
    return [x.strip() for x in content]