#!coding: utf-8
import psyco
from Isolated_Char_Generator import *

DEFAULT_SIZE = (38, 31)
SEUIL = 200

GENERATE_TRAINING_SET = True
GENERATE_VALIDATION_SET = True

FONTS = ["Fonts/califb.ttf", "Fonts/vera.ttf"]


if GENERATE_TRAINING_SET:
    print """
    ##############################################################################
    #########################   TRAINING    SET   ################################
    ##############################################################################
    """
    
    #GENERATE_CAPITAL_LETTERS = True
    #GENERATE_DIGITS = True
    #elem_to_gen = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)
    
    elem_to_gen=['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'T', '2', '3']
    elem_to_gen=['A', 'B', 'D', 'E', 'M', 'T', '2', '3']
    
    DESTINATION_FOLDER = 'Hotmail/DBTraining'
    CLEAN_DESTINATION_FOLDER = True
    DISTORTION_W_MIN = 0
    DISTORTION_W_MAX = 7
    DISTORTION_H_MIN = 0
    DISTORTION_H_MAX = 7
    SCALE_MIN = 25
    SCALE_MAX = 31
    STEP = 1
    ALIGN_RANGEY = [0.1, 0.5, 0.9]
    ALIGN_RANGEX = [0.5]
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                 DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, SEUIL)


if GENERATE_VALIDATION_SET:
    print """
    ##############################################################################
    ###########################   TEST   SET      ################################
    ##############################################################################
    """
    
    #GENERATE_CAPITAL_LETTERS = True
    #GENERATE_DIGITS = True
    #elem_to_gen = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)
    
    elem_to_gen=['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'T', '2', '3']
    elem_to_gen = ['A', 'B', 'D', 'E', 'M', 'T', '2', '3']
    
    DESTINATION_FOLDER = 'Hotmail/DBTest'
    CLEAN_DESTINATION_FOLDER = True
    DISTORTION_W_MIN = 0
    DISTORTION_W_MAX = 7
    DISTORTION_H_MIN = 0
    DISTORTION_H_MAX = 7
    SCALE_MIN = 25
    SCALE_MAX = 30
    STEP = 2
    ALIGN_RANGEY = [0.1, 0.5, 0.9]
    ALIGN_RANGEX = [0.5]
    
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                 DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, SEUIL)









