#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# *udacity-dog-breed-project/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-05-07
# REVISED DATE: 2021-05-07
# TODO 5: Define calculates_results_stats function

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
    """

    stats_dic = {'cnt_images':len(results_dic),'cnt_label_match':0,'cnt_images_not':0,\
    'cnt_images_dog':0,'cnt_correct_dog':0,'cnt_correct_not':0,'cnt_correct_breed':0,\
    'pct_label_match':0,'pct_correct_dog':0,'pct_correct_not':0,'pct_correct_breed':0}

    for key in results_dic:
        if results_dic[key][2] == "1":
            stats_dic['cnt_label_match'] += 1
        if results_dic[key][3] == "1":
            stats_dic['cnt_images_dog'] += 1
        if results_dic[key][3] and results_dic[key][4] == "1":
            stats_dic['cnt_correct_dog'] += 1
        if results_dic[key][3] and results_dic[key][4] == "0":
            stats_dic['cnt_correct_not'] += 1
        if results_dic[key][2] and results_dic[key][3] == "1":
            stats_dic['cnt_correct_breed'] += 1

    stats_dic['cnt_images_not'] = stats_dic['cnt_images']-stats_dic['cnt_images_dog']

    if stats_dic['cnt_images'] != '0':
        stats_dic['pct_label_match'] = 100*stats_dic['cnt_label_match']/stats_dic['cnt_images']
    else:
        stats_dic['pct_label_match'] = 0
    if stats_dic['cnt_images_dog'] != '0':
        stats_dic['pct_correct_dog'] = 100*stats_dic['cnt_correct_dog']/stats_dic['cnt_images_dog']
    else:
        stats_dic['pct_correct_dog'] = 0
    if stats_dic['cnt_images_not'] != '0':
        stats_dic['pct_correct_not'] = 100*stats_dic['cnt_correct_not']/stats_dic['cnt_images_not']
    else:
        stats_dic['pct_correct_not'] = 0
    if stats_dic['cnt_images_dog'] != '0':
        stats_dic['pct_correct_breed'] = 100*stats_dic['cnt_correct_breed']/stats_dic['cnt_images_dog']
    else:
        stats_dic['pct_correct_breed'] = 0

    for key in stats_dic:
        print('\nName = ',key,'\nValue = ',stats_dic[key])

    return stats_dic
