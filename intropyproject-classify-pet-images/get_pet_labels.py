#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filename_list = listdir(image_dir) #Create a list of all filenames in the folder returned from get_input arguments
    filename_word_list = listdir(image_dir) #Repeat above to create a list ready for manipulation into individual words
    pet_name_list = [] #Create empty list to allow for formatted pet names to be inputted
    pets_dic = dict() #Prepare pets dictionary to compile final results

    for i in range(0,len(filename_word_list),1): #Iterate through the list of filenames
        if filename_word_list[i][0] != ".":
            pet_name_list.append('') #Add a new slot for a new iteration of name formatting to eventually occupy
            filename_word_list[i] = filename_word_list[i].lower() #Reformat filenames to lowercase
            filename_word_list[i] = filename_word_list[i].split('_') #Splite each filenames into individual words
            for word in filename_word_list[i]: #Move through split words from the filename getting looped
                if word.isalpha(): #Add the alpha word to the pet name and ignore numbers and characters
                    pet_name_list[i] += word + ' '
            pet_name_list[i] = pet_name_list[i].strip() #Remove the extra space added from the line above
            if filename_list[i] not in pets_dic: #Add the filename as a key and the pet name as a value if it doesn't exist in dictionary
                pets_dic[filename_list[i]] = pet_name_list[i]
            else: #Print notice message if the item exists already
                print('**Notice: Key = ', filename_list[i],' already exists in pets_dic with Value = ', pets_dic[filename_list[i]],'**')

    print('Printing key-value pairs in pets_dic:')
    for key in pets_dic: #Print generated dictionary
        print('Filename = ', key, '    Value = ', pets_dic[key])

    return pets_dic
