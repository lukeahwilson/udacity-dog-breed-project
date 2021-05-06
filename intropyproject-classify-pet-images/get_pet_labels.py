#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# *udacity-dog-breed-project/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-04-27
# REVISED DATE: 2021-05-03
# TODO 2: Define get_pet_labels function

from os import listdir # Imports python modules

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
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
            filename_word_list[i] = filename_word_list[i].lower().split('_') #Reformat filenames to lowercase and split each filename into individual words
            for word in filename_word_list[i]: #Move through split words from the filename getting looped
                if word.isalpha(): #Add the alpha word to the pet name and ignore numbers and characters
                    pet_name_list[i] += word + ' '
            pet_name_list[i] = pet_name_list[i].strip() #Remove the extra space added from the line above
            if filename_list[i] not in pets_dic: #Add the filename as a key and the pet name as a value if it doesn't exist in dictionary
                pets_dic[filename_list[i]] = [pet_name_list[i]] #Make sure it makes the value a list and not a string
            else: #Print notice message if the item exists already
                print('**Notice: Key = ', filename_list[i],' already exists in pets_dic with Value = ', pets_dic[filename_list[i]],'**')
                
    return pets_dic
