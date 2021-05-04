#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# *udacity-dog-breed-project/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-04-22
# REVISED DATE: 2021-04-22
# TODO 1: Define get_input_args function

import argparse #import python argparse function

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to create and define these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    
    parser = argparse.ArgumentParser() #define argument parser
    parser.add_argument('--dir', type=str, default='pet_images/', help='path to the folder of pet images') #create directory argument
    parser.add_argument('--arch', type=str, default='vgg', help='choose between \'resnet\', \'alexnet\' or \'vgg\' architectures') #create architecture choice argument
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='name of the file containing the list of dognames') #create dogfile argument

    return parser.parse_args() #return parsed arguments
