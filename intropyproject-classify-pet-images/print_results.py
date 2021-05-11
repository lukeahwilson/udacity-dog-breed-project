#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# *udacity-dog-breed-project/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-05-11
# REVISED DATE: 2021-05-11
# TODO 6: Define print_results function
#
def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """

    print('\n***PRINTING ', model.upper(), 'ARCHITECTURE RESULTS DICTIONARY***')
    for key in results_dic: # Work through each key in the dictionary and print information
        print('\nKey is Filename = {}\n0 Image Label = {}\n1 Classifier Label = {}\n2 Label Match = {}\n3 Image Label Confirmed = {}\n4 Classifier Label Confirmed = {}'.format(\
              key, results_dic[key][0], results_dic[key][1], results_dic[key][2], results_dic[key][3], results_dic[key][4]))

    print('\n***PRINTING ', model.upper(), 'ARCHITECTURE MISCLASSIFICATIONS***')
    for key in results_dic: # Work through each key in the dictionary
        if results_dic[key][3] == 1: # Image is dog but
            if results_dic[key][4] == 0 and print_incorrect_dogs == True: # Classifier thinks it is not
                print('\nThe {} architecture has failed to identify {} as a dog'.format(model, key))
            elif results_dic[key][2] == 0 and print_incorrect_breed == True: # Classifier gave it wrong breed
                print('\nThe {} architecture has failed to identify {} by the correct breed'.format(model, key))
        if results_dic[key][3] == 0 and results_dic[key][4] == 1 and print_incorrect_dogs == True: # Image is not dog but classifier thinks it is
            print('\nThe {} architecture has wrongly identified {} as a dog'.format(model, key))

    print('\n***PRINTING ', model.upper(), 'ARCHITECTURE STATISTICS***')
    for key in results_stats_dic: # Print Key Value Pairs for stats
        print('\nStatistic Name = ',key,'\nValue = ',results_stats_dic[key])

    None
